from django.db import models

# basicamente isso aqui é uma classe que vai virar uma tabela no banco de dados
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome