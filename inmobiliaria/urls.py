"""
URL configuration for inmobiliaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from propiedades import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta para la página principal
    path('', views.index, name='home'),
    path('admin-dashboard/', views.index_admin, name='index_admin'),  # Ruta opcional para la vista admin

    # Ruta para iniciar sesión
    path('login/', auth_views.LoginView.as_view(template_name='Iniciar_session.html'), name='login'),
   
    # Aquí definimos la URL con nombre 'register'
    path('register/', views.register, name='register'),  
    
    # Definir el patrón de URL para 'index'
    path('', views.index, name='index'),
    
    # Ruta para crear una propiedad
    path('agregar-propiedad/', views.agregar_propiedad, name='agregar_propiedad'),

    # Ruta para editar una propiedad
    path('editar-propiedad/<int:pk>/', views.editar_propiedad, name='editar_propiedad'),
]
