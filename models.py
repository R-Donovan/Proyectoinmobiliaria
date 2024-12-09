from django.db import models

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
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
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
