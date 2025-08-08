from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm

# VISTA DE BIENVENIDA
def welcome(request):
    return render(request, 'registro/welcome.html')

# DASHBOARD (requiere login)
@login_required
def dashboard_view(request):
    return render(request, 'registro/index.html')
def index2_view(request):
    return render(request, 'registro/index2.html')

def index3_view(request):
    return render(request, 'registro/index3.html')

# --- Vista de LOGIN ---
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'registro/login.html')

# --- Vista de REGISTRO ---
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente")
            return redirect('login')  # Cambia 'login' por el nombre real de tu ruta
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = RegistroForm()

    return render(request, 'registro/register.html', {'form': form})