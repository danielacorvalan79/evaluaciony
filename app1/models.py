from django.db import models
from django.db import models


# Create your models here.

class Paciente(models.Model):
    run = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    telefono = models.IntegerField()
    patologias = models.CharField(max_length=2000)

class Examen(models.Model):
    run = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    resultado = models.CharField(max_length=50)

    def __str__(self):
        return self.run
        
class Medicamento(models.Model):
    fecha_indicacion = models.DateField()
    nombre = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)