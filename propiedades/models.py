from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, choices=[('dueño', 'Dueño'), ('admin', 'Admin')])
    # Agrega cualquier otro campo que sea necesario

    def __str__(self):
        return self.user.username

class Dueno(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Propiedad(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=255)
    no_habitaciones = models.IntegerField()
    no_banos = models.IntegerField()
    tamano = models.DecimalField(max_digits=10, decimal_places=2)
    dueno = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='propiedades/', null=True, blank=True)

    def __str__(self):
        return str(self.titulo) if self.titulo else "Sin título"