from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Produto


def home(request):
    produtos = Produto.objects.all()
    return render(request, "home_produto.html", {"produtos": produtos})

def detalhe_produto(request: HttpRequest, codigo: int) -> HttpResponse:
    try:
        produto = Produto.objects.get(codigo=codigo)
        return render(request, "detalhe_produto.html", {"produto": produto})
    except Produto.DoesNotExist:
        return HttpResponse("Produto não encontrado", status=404)
    
def adicionar_carrinho(request: HttpRequest, codigo: int) -> HttpResponse:
    produto = get_object_or_404(Produto, codigo=codigo)

    carrinho = request.session.get('carrinho', {})

    if str(codigo) in carrinho:
        carrinho[str(codigo)] += 1
    else:
        carrinho[str(codigo)] = 1

    request.session['carrinho'] = carrinho
    request.session.modified = True

    return redirect('home_produto')
    
def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos = Produto.objects.filter(codigo__in=carrinho.keys())

    itens = []
    total = 0

    for produto in produtos:
        quantidade = carrinho[str(produto.codigo)]
        subtotal = produto.preco * quantidade
        total += subtotal

        itens.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

    return render(request, "carrinho.html", {
        "itens": itens,
        "total": total
    })

def remover_carrinho(request, codigo):
    carrinho = request.session.get('carrinho', {})

    if str(codigo) in carrinho:
        del carrinho[str(codigo)]
        request.session['carrinho'] = carrinho
        request.session.modified = True

    return redirect('ver_carrinho')