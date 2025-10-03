from django.db import models
from cliente.models import Cliente
from produto.models import Produto  # Ajuste o caminho conforme seu app

class Pedido(models.Model):
    STATUS_CHOICES = [
        ("CR", "Criado"),
        ("PG", "Pago"),
        ("EN", "Enviado"),
        ("CO", "Concluído"),
        ("CA", "Cancelado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="CR")
    forma_pagamento = models.CharField(max_length=50, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome} ({self.get_status_display()})"

    def calcular_total(self):
        total = sum(item.subtotal for item in self.itens.all())
        self.valor_total = total
        self.save()
        return total


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Itens de Pedido"

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido #{self.pedido.id})"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)
        self.pedido.calcular_total()