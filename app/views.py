from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django import forms
from .forms import UsuarioForm
# Create your views here.
def home(request):
    return render(request, 'home.html')


def hello_view(request):
    return HttpResponse("Olá django")

def listar_pessoas(request):
    pessoas = Usuario.objects.all()
    return render(request, 'list.html', {"pessoas": pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = UsuarioForm()
    return render(request, 'create.html', {'usuario': form})



def deletar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_pessoas')
    return render(request, 'confirmar_delete.html', {'usuario': usuario})

def atualizar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'create.html', {'usuario': form})