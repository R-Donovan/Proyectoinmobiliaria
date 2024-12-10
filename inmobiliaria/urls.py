from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_propiedad, name='agregar_propiedad'),
    path('editar/<int:propiedad_id>/', views.editar_propiedad, name='editar_propiedad'),
]
