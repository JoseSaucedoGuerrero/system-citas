# 🏥 System Citas - Sistema de Gestión de Citas Médicas

Sistema web desarrollado en Django para la gestión  de citas médicas.

## 📋 Características

### Para Pacientes
- ✅ Registro e inicio de sesión
- ✅ Búsqueda avanzada de doctores (por nombre, especialidad)
- ✅ Visualizar disponibilidad de doctores
- ✅ Agendar citas médicas
- ✅ Ver historial de citas
- ✅ Cancelar citas
- ✅ Ver detalles de consultas (diagnóstico, tratamiento)

### Para Doctores
- ✅ Dashboard con estadísticas personales
- ✅ Agenda completa con filtros
- ✅ Gestión de horarios de atención
- ✅ Atender pacientes (registrar diagnóstico y tratamiento)
- ✅ Ver historial completo de pacientes
- ✅ Confirmar/rechazar citas
- ✅ Gestionar excepciones (vacaciones, bloqueos)

### Para Administradores
- ✅ Dashboard administrativo con métricas del sistema
- ✅ Reportes detallados (citas, doctores, pacientes)
- ✅ Estadísticas y gráficos
- ✅ Gestión completa del sistema

## 🚀 Tecnologías Utilizadas

- **Backend:** Python 3.11+ | Django 5.0
- **Base de Datos:** PostgreSQL
- **Frontend:** HTML5 | CSS3 | Bootstrap 5
- **Otros:** Django ORM | Font Awesome

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/system-citas.git
cd system-citas
```

### 2. Crear entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Crear base de datos en PostgreSQL:
```sql
CREATE DATABASE system_citas
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C';
```

Configurar credenciales en `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'system_citas',
        'USER': 'postgres',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor
```bash
python manage.py runserver
```

Acceder a: `http://127.0.0.1:8000`

## 📊 Estructura del Proyecto
```
system-citas/
├── config/              # Configuración del proyecto
├── usuarios/            # Gestión de usuarios y autenticación
├── doctores/            # Gestión de doctores
├── pacientes/           # Gestión de pacientes
├── citas/               # Gestión de citas (CORE)
├── especialidades/      # Catálogo de especialidades médicas
├── horarios/            # Horarios y disponibilidad
├── reportes/            # Dashboards y reportes
├── templates/           # Templates HTML globales
├── static/              # Archivos estáticos (CSS, JS, imágenes)
└── media/               # Archivos subidos por usuarios
```

## 🔐 Usuarios de Prueba

- **Admin:** admin / admin123
- **Doctor:** Antonio/joseS415---josue/doctor123---carlos/doctor123
- **Paciente:** mike/joseS415----

## 🎯 Validaciones Implementadas

- ❌ No se pueden agendar citas en fechas pasadas
- ❌ No se pueden agendar citas fuera del horario laboral
- ❌ No se permite doble reserva del mismo horario
- ❌ Validación de días laborables del doctor
- ❌ Validación de excepciones (vacaciones, bloqueos)

## 📝 Licencia

Este proyecto fue desarrollado con fines educativos.

## 👨‍💻 Autor

Desarrollado por [Saucedo Guerrero Jose Dilmer]

---
