from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Propiedad
from .forms import PropiedadForm

# Página principal
def index(request):
    propiedades = Propiedad.objects.all()

    # Filtrar por precio y ubicación si se proporcionan
    precio_max = request.GET.get('precio_max')
    ubicacion = request.GET.get('ubicacion')
    if precio_max:
        propiedades = propiedades.filter(precio__lte=precio_max)
    if ubicacion:
        propiedades = propiedades.filter(ubicacion__icontains=ubicacion)

    return render(request, 'index.html', {'propiedades': propiedades})

# Crear nueva propiedad (solo para dueños y admin)
@user_passes_test(lambda user: user.is_staff or hasattr(user, 'dueno'))
def agregar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save(commit=False)
            # Asociar la propiedad con el dueño actual (si es dueño)
            if hasattr(request.user, 'dueno'):
                propiedad.dueno = request.user.dueno
            propiedad.save()
            return redirect('index')
    else:
        form = PropiedadForm()
    return render(request, 'agregar_propiedad.html', {'form': form})

# Editar una propiedad
@user_passes_test(lambda user: user.is_staff or hasattr(user, 'dueno'))
def editar_propiedad(request, propiedad_id):
    propiedad = Propiedad.objects.get(id=propiedad_id)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'editar_propiedad.html', {'form': form, 'propiedad': propiedad})
