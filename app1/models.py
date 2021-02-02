from django.db import models

# Create your models here.

# Create your models here.
class Administrador(models.Model):
    usuario = models.CharField(primary_key = True, max_length=30)
    contraseña = models.CharField(max_length=20)


class Usuarios(models.Model):
    usuario = models.CharField(primary_key = True, max_length=30)
    contraseña = models.CharField(max_length=20)

class Paciente(models.Model):
    run = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    telefono = models.IntegerField()
    patologias = models.CharField(max_length=2000)

class ExamenHemograma(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hematocrito = models.DecimalField(max_digits=5, decimal_places=2)
    hemoglobina = models.DecimalField(max_digits=5, decimal_places=2)


class ExamenPerfill(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    colesterol_total = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    trigliceridos = models.DecimalField(max_digits=5, decimal_places=2, blank = True)    


class ExamenPerfilb(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    glucosa = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    bilirrubina_total = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    

class Medicamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_indicacion = models.DateField()
    nombre = models.CharField(max_length=50)
    hora = models.TimeField()
    dosis = models.CharField(max_length=50)
