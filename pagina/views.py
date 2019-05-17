from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def cargarInicio(request):
    return render(request, 'pagina/base.html')

def cargarLogin(request):
    return render(request, 'pagina/login.html')

def cargarRegistro(request):
	return render(request, 'pagina/registro.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/pagina/inicio')
    else:
        form = UserCreationForm()
    return render(request, 'pagina/registro.html', {'form': form})
