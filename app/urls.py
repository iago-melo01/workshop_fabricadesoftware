from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name ='home'),
    path('hello/', views.hello_view, name='hello'),
    path('listar/', views.listar_pessoas, name="listar_pessoas"),
    path('criar/', views.criar_pessoa, name='criar_pessoa'),
    path('deletar/<int:pk>', views.deletar_usuario, name='deletar_pessoa'),
    path('atualizar/<int:pk>', views.atualizar_usuario, name="atualizar_pessoa"),

]