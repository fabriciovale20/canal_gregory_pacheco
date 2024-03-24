from django.shortcuts import render, redirect
from .models import Pessoa

# Função da página inicial
def home(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'index.html', {'pessoas': pessoas})

# Função de Salvar
def salvar(request):
    vnome = request.POST.get('nome')
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()

    return render(request, 'index.html', {'pessoas': pessoas})

# Função de Editar
def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)

    return render(request, 'update.html', {'pessoa': pessoa})

# Função de Update
def update(request, id):
    vnome = request.POST.get('nome')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()

    return redirect(home)

# Função de Deletar
def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    
    return redirect(home)
    