from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create new user.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')

        user = User.objects.filter(username=username)
        if user.exists():
            return redirect('/usuarios/cadastro/')

        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não conferem.')
            return redirect('/usuarios/cadastro/')
        else:
            try:
                user = User.objects.create_user(username=username, password=senha)
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
                return redirect('/usuarios/logar')
            except:
                messages.add_message(request, constants.ERROR, 'Erro ao cadastrar usuário.')
                return redirect('/usuarios/cadastro/')
            
# Login user.
def logar (request):
    if(request.method == 'GET'):
        return render(request, 'login.html')
    elif(request.method == 'POST'):
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=username, password=senha)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado com sucesso.')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos.')
            return redirect('/usuarios/logar/')
        
# Logout user.
def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.SUCCESS, 'Deslogado com sucesso.')
    return redirect('/usuarios/logar/')