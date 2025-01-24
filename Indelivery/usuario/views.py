from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect 
from hashlib import sha256 
from .models import Usuario 


def home(requests):
    return HttpResponse('Olá')

def cadastrar(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':

        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status': status})
    
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        usuario_banco = Usuario.objects.filter(nome=username) 
        if len(usuario_banco) > 0:
            return redirect('/auth/cadastro?status=1')
        
        if len(password) < 8:
            return redirect('/auth/cadastro?status=2')
        
        try:
            password = sha256(password.encode()).hexdigest()
            usuario = Usuario(
                nome = username,
                senha = password,
                email = email
                )
            usuario.save()
            return redirect('/auth/cadastro?status=0')
        except:
            return redirect('/auth/cadastro')

    
def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'login.html', {'status': status})
    else:
        user = request.POST['username']
        password = request.POST['password']


        password = sha256(password.encode()).hexdigest()
        usuario = Usuario.objects.filter(nome = user).filter(senha = password)
        if len(usuario) == 0:
            return redirect('/auth/login?status=1')
        elif len(usuario) > 0:
            request.session['usuario'] = usuario[0].id
            return redirect('/produto/home/')
        
# função de logout
def logout(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return redirect('/auth/login')