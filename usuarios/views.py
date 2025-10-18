from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario
from pacientes.models import Paciente

def home(request):
    """Página de inicio"""
    return render(request, 'home.html')

def login_view(request):
    """Vista de login"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.get_full_name()}!')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')

def registro_view(request):
    """Vista de registro"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        # Datos del usuario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telefono = request.POST.get('telefono')
        
        # Datos del paciente
        dni = request.POST.get('dni')
        
        # Validaciones
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuarios/registro.html')
        
        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return render(request, 'usuarios/registro.html')
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado.')
            return render(request, 'usuarios/registro.html')
        
        if Paciente.objects.filter(dni=dni).exists():
            messages.error(request, 'El DNI ya está registrado.')
            return render(request, 'usuarios/registro.html')
        
        # Crear usuario
        user = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            telefono=telefono,
            rol='paciente'
        )
        
        # Crear paciente
        Paciente.objects.create(
            usuario=user,
            dni=dni
        )
        
        messages.success(request, '¡Registro exitoso! Ya puedes iniciar sesión.')
        return redirect('login')
    
    return render(request, 'usuarios/registro.html')

def logout_view(request):
    """Vista de logout"""
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')