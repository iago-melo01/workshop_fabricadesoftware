from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name ='home'),
    path('hello/', views.hello_view, name='hello'),
    path('listar/', views.listar_pessoas),
    path('criar/', views.criar_pessoa),
]