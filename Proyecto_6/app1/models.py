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

class ExamenHemograma(models.Model):
    fecha = models.DateField()
    hematocrito = models.DecimalField(max_digits=5, decimal_places=2)
    hemoglobina = models.DecimalField(max_digits=5, decimal_places=2)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class ExamenPerfill(models.Model):
    fecha = models.DateField()
    colesterol_total = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    trigliceridos = models.DecimalField(max_digits=5, decimal_places=2, blank = True)    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class ExamenPerfilb(models.Model):
    fecha = models.DateField()
    glucosa = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    bilirrubina_total = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Medicamento(models.Model):
    codigo = models.CharField(max_length=8, primary_key=True)
    fecha_indicacion = models.DateField()
    nombre = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
