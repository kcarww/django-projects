from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_produto"),
    path('<int:codigo>/', views.detalhe_produto, name="detalhe_produto"),
    path("carrinho/adicionar/<int:codigo>/", views.adicionar_carrinho, name="adicionar_carrinho"),
    path("carrinho/", views.ver_carrinho, name="ver_carrinho"),
    path("carrinho/remover/<int:codigo>/", views.remover_carrinho, name="remover_carrinho"),
]
