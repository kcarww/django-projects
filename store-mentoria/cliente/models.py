from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
    def set_senha(self, senha_raw):
        self.senha = make_password(senha_raw)

    def verificar_senha(self, senha_raw):
        return check_password(senha_raw, self.senha)
