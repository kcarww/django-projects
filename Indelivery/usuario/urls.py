from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("cadastro", views.cadastrar, name='cadastro'),
    path("login", views.login, name='login'),
    path('logout', views.logout, name = 'logout'), # view de logout
]
