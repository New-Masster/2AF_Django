from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Funcionario

def list_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/list_funcionarios.html', {'funcionarios': funcionarios})

def view_funcionario(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)
    return render(request, 'funcionarios/view_funcionario.html', {'funcionario': funcionario})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_funcionarios')
        else:
            return render(request, 'funcionarios/login.html', {'error_message': 'Invalid login'})
    return render(request, 'funcionarios/login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'funcionarios/register_user.html', {'form': form})

@login_required
def logout(request):
    logout(request)
    return redirect('login')
