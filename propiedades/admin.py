from django.contrib import admin
from .models import Propiedad, UserProfile, Dueno

# Configuración para mostrar el modelo Propiedad en el admin
@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'ubicacion', 'no_habitaciones', 'no_banos', 'tamano', 'dueno')
    search_fields = ('titulo', 'ubicacion', 'dueno__nombre')
    list_filter = ('precio', 'no_habitaciones', 'no_banos')

# Configuración para mostrar el modelo UserProfile en el admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol')
    search_fields = ('user__username', 'rol')

# Configuración para mostrar el modelo Dueno en el admin
@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'telefono', 'direccion')
    search_fields = ('nombre', 'apellido', 'correo')
