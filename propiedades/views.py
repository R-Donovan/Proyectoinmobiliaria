from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from propiedades.models import Propiedad
from propiedades.forms import PropiedadForm

# Página principal (index.html)
def index(request):
    propiedades = Propiedad.objects.all()
    if request.user.is_authenticated and request.user.userprofile.rol in ['dueño', 'admin']:
        return render(request, 'indexDA.html', {'propiedades': propiedades})
    return render(request, 'index.html', {'propiedades': propiedades})

# Vista específica para dueños/admins (si usas una ruta aparte como /admin-dashboard/)
def index_admin(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'indexDA.html', {'propiedades': propiedades})

# Vista para crear cuenta
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente después de registrar
            login(request, user)
            return redirect('index')  # Redirigir a la página principal después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    
# Vista para iniciar sesión (Iniciar_session.html)
class CustomLoginView(LoginView):
    template_name = 'Iniciar_session.html'


# Vista para agregar una propiedad (Formulario_de_casa.html)
@login_required
def agregar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save(commit=False)
            propiedad.dueno = request.user.userprofile.dueno  # Asigna el dueño como el usuario actual
            propiedad.save()
            return redirect('index')
    else:
        form = PropiedadForm()
    return render(request, 'Formulario_de_casa.html', {'form': form})

# Vista para editar una propiedad (Editar_Propiedad.html)
@login_required
def editar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk, dueno=request.user.userprofile.dueno)  # Asegura que la propiedad pertenece al dueño
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'Editar_Propiedad.html', {'form': form, 'propiedad': propiedad})
