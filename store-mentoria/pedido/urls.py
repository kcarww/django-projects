from django.urls import path
from . import views

urlpatterns = [
    path("resumo/", views.resumo_pedido, name="resumo_pedido"),
    path("finalizar-pedido/", views.confirmar_pedido, name="finalizar_pedido"),
    path("obrigado/<int:pk>/", views.obrigado_pedido, name="obrigado_pedido"),
    path("<int:pk>/", views.detalhe_pedido, name="detalhe_pedido"),
]
