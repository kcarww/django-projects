from django.shortcuts import redirect

class ClienteAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        rotas_publicas = ['/cliente/login', '/cliente/registrar']
                
        if not any(request.path.startswith(rota) for rota in rotas_publicas):
            if 'cliente_id' not in request.session:
                return redirect('login')
        
        return self.get_response(request)   