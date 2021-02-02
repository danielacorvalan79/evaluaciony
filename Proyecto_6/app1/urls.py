from django.urls import path
from . import views

app_name="app1"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home),
    path('exams/', views.exams),
    path('meds/', views.meds),
    path('cal/', views.cal, name='cal'),
    path('lista/', views.ListaPaciente.as_view(), name='lista'),
    path('crear/', views.CrearPaciente.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
    path('examenes/', views.ExamenesView.as_view(), name='examenes'),
    #path('agregar_examenh/', views.AgregarExamenh.as_view(), name='agregar_examen'),
    #path('<int:pk>/eliminar_examenh', views.EliminarExamenh.as_view(), name='eliminar_examen'),
    #path('crear_examenpl/', views.AgregarExamenpl.as_view(), name='agregar_examen'),
    #path('<int:pk>/eliminar_examenh', views.EliminarExamenpl.as_view(), name='eliminar_examen'),
    #path('crear_examenpb/', views.AgregarExamenpb.as_view(), name='agregar_examen'),
    #path('<int:pk>/eliminar_examenpb', views.EliminarExamenpb.as_view(), name='eliminar_examen'),
    path('lista_medicamentos/', views.ListaMedicamentos.as_view(), name='lista_medicamentos'),
    path('agregar_medicamento/', views.AgregarMedicamento.as_view(), name='agregar_medicamento'),
    path('<int:pk>/editar', views.EditarMedicamento.as_view(), name='editar_medicamento'),    
    path('<int:pk>/eliminar_medicamento', views.EliminarMedicamento.as_view(), name='eliminar_medicamento'),
]
