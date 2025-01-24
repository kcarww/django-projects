from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("categoria/<int:id>", views.categorias, name='categoria'),
    path("produto/<int:id>", views.produto, name='produto'),
]

