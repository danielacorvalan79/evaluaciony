from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.urls import reverse


app_name="app1"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('home/', views.home, name='home'),
    path('main/', views.home, name='main'),
    path('exams/', views.exams, name='examenes'),
    path('cal/', views.cal, name='cal'),
    path('lista/', views.ListaPaciente.as_view(), name='lista'),
    path('crear/', views.CrearPaciente.as_view(), name='crear'),
    path('agregar_paciente/', views.AgregarPaciente.as_view(), name='agregar'),
    #path('agregar_paciente/', views.AgregarPaciente.as_view(), name='agregar'),
    path('<int:pk>/paciente_per', views.PacientePersonalizado.as_view(), name='paciente_per'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
    path('lista_medicamentos/', views.ListaMedicamentos.as_view(), name='lista_medicamentos'),
    path('agregar_medicamento/', views.AgregarMedicamento.as_view(), name='agregar_medicamento'),
    path('<int:pk>/editar_medicamento', views.EditarMedicamento.as_view(), name='editar_medicamento'),    
    path('<int:pk>/eliminar_medicamento', views.EliminarMedicamento.as_view(), name='eliminar_medicamento'),
    path('inicio1/', views.inicio1.as_view(), name = 'inicio1'),

]
