from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.db import transaction
from cliente.models import Cliente
from produto.models import Produto
from .models import Pedido, ItemPedido

def resumo_pedido(request: HttpRequest) -> HttpResponse:
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect('home_produto')

    produtos = []
    total = 0
    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(codigo=int(produto_id))
        subtotal = produto.preco * quantidade
        produtos.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal,
        })
        total += subtotal

    return render(request, "resumo_pedido.html", {
        "produtos": produtos,
        "total": total,
    })


@transaction.atomic
def confirmar_pedido(request):
    if request.method != "POST":
        return redirect("resumo_pedido")

    carrinho = request.session.get("carrinho", {})
    if not carrinho:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect("home_produto")

    cliente_id = request.session.get("cliente_id")
    if not cliente_id:
        messages.error(request, "Você precisa estar logado para finalizar.")
        return redirect("login")

    cliente = Cliente.objects.get(id=cliente_id)

    forma_pagamento = request.POST.get("forma_pagamento", "Não definido")

    pedido = Pedido.objects.create(cliente=cliente, forma_pagamento=forma_pagamento)

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(codigo=int(produto_id))
        ItemPedido.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=int(quantidade),
            preco_unitario=produto.preco,
        )

    pedido.calcular_total()

    request.session['carrinho'] = {}
    request.session.modified = True

    messages.success(request, f"Pedido #{pedido.id} criado com sucesso!")
    return redirect("obrigado_pedido", pedido.id)


def obrigado_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, cliente__id=request.session.get("cliente_id"))
    return render(request, "obrigado_pedido.html", {"pedido": pedido})

def detalhe_pedido(request, pk):
    pedido = get_object_or_404(
        Pedido, pk=pk, cliente__id=request.session.get("cliente_id")
    )
    return render(request, "detalhe_pedido.html", {"pedido": pedido})