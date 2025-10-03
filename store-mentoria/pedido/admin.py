from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    readonly_fields = ('subtotal',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "status", "forma_pagamento", "valor_total", "data_pedido")
    list_filter = ("status", "forma_pagamento", "data_pedido")
    search_fields = ("cliente__nome", "cliente__email")
    readonly_fields = ("valor_total", "data_pedido")
    inlines = [ItemPedidoInline]

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade", "preco_unitario", "subtotal")
    readonly_fields = ("subtotal",)