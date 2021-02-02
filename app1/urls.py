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
    path('agregar_hemograma/<pk>/', views.AgregarHemograma.as_view(), name='agregar_hemograma'),
    path('agregar_perfill/<pk>/', views.AgregarPerfill.as_view(), name='agregar_perfill'),
    path('agregar_perfilb/<pk>/', views.AgregarPerfilb.as_view(), name='agregar_perfilb'),
    path('lista_medicamentos/', views.ListaMedicamentos.as_view(), name='lista_medicamentos'),
    path('agregar_medicamentos/', views.AgregarMedicamento.as_view(), name='agregar_medicamentos'),
    path('<int:pk>/editar_medicamento', views.EditarMedicamento.as_view(), name='editar_medicamento'),    
    path('<int:pk>/eliminar_medicamento', views.EliminarMedicamento.as_view(), name='eliminar_medicamento'),

    path('medicamentos', views.MedicamentoView.as_view(), name='medicamentos'),
    path('agregar_medicamento/', views.AgregarMedicamento.as_view() , name='agregar_medicamento' ),
    #path('', views.Login.as_view(), name='login' ),
    #path('registro/', views.Registro.as_view() , name='registro' ),
    #path('editar/<pk>/', views.Editar.as_view() , name='editar' ),
    #path('borrar/<pk>/', views.BorrarUsuario.as_view() , name='borrar' ),

    path('home/', views.Home.as_view(), name="Home"),
    path('editarh/<slug:pk>/', views.EditarPaciente.as_view() , name="editarh"),
    path('admin/', views.Home.as_view(), name="admin"),

]
