from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente

def registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        senha = request.POST.get('senha')
        telefone = request.POST.get('telefone')
        
        cliente = Cliente(
            nome=nome,
            email=email,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone
        )
        cliente.set_senha(senha) 
        cliente.save()
        
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    
    return render(request, 'registrar_usuario.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            cliente = Cliente.objects.get(email=email, ativo=True)
            if cliente.verificar_senha(senha):
                request.session['cliente_id'] = cliente.id
                messages.success(request, f'Bem-vindo, {cliente.nome}!')
                return redirect('home_produto')
            else:
                messages.error(request, 'Senha incorreta!')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado!')
    
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')