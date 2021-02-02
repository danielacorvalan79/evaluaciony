from django.shortcuts import render
from django.views.generic import ListView, View
from django.views import generic
from .models import Paciente, ExamenHemograma, ExamenPerfill, ExamenPerfilb, Medicamento
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 


# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def home(request):
    return render(request, 'app1/main.html') 

def register(request):
    return render(request, 'app1/registro.html')  

def exams(request):
    return render(request, 'app1/examenes.html') 

def meds(request):
    return render(request, 'app1/medicamento.html')

def cal(request):
    return render( request, 'app1/calendario.html')



class Inicio(generic.TemplateView):
    template_name = 'app1/index.html'


class ListaPaciente(ListView):
    model=Paciente
    template_name = 'app1/lista_paciente.html'
    context_object_name = 'paciente'


class CrearPaciente(CreateView):
    model=Paciente
    template_name = 'app1/crear_paciente.html'
    fields='__all__'
    success_url= reverse_lazy('app1:lista')


class EditarPaciente(UpdateView):
    model=Paciente
    template_name = 'app1/editar_paciente.html'
    fields='__all__'
    success_url=reverse_lazy('app1:lista')


class EliminarPaciente(DeleteView):
    model=Paciente
    template_name = 'app1/eliminar_paciente.html'
    fields='__all__'
    success_url=reverse_lazy('app1:lista')
    context_object_name = 'paciente'


class ExamenesView(View):
    template_name = 'app1/examenes.html'
    success_url = 'app1:examenes'

class ListaExamenesH(ListView):
    model=ExamenHemograma
    template_name = 'app1/examenes.html'
    context_object_name = 'examen'

class AgregarExamenh(CreateView):
    model=ExamenHemograma
    template_name = 'app1/agregar_examen.html'
    fields='__all__'
    success_url= reverse_lazy('app1:examenes')

class EliminarExamenh(DeleteView):
    model=ExamenHemograma
    template_name = 'app1/eliminar_examen.html'
    fields='__all__'
    success_url=reverse_lazy('app1:examenes')
    context_object_name = 'examen'

class ListaExamenespl(ListView):
    model=ExamenPerfill
    template_name = 'app1/examenes.html'
    context_object_name = 'examen'

class AgregarExamenpl(CreateView):
    model=ExamenPerfill
    template_name = 'app1/agregar_examen.html'
    fields='__all__'
    success_url= reverse_lazy('app1:examenes')

class EliminarExamenpl(DeleteView):
    model=ExamenPerfill
    template_name = 'app1/eliminar_examen.html'
    fields='__all__'
    success_url=reverse_lazy('app1:examenes')
    context_object_name = 'examen'

class ListaExamenespb(ListView):
    model=ExamenPerfilb
    template_name = 'app1/examenes.html'
    context_object_name = 'examen'

class AgregarExamenpb(CreateView):
    model=ExamenPerfilb
    template_name = 'app1/agregar_examen.html'
    fields='__all__'
    success_url= reverse_lazy('app1:examenes')

class EliminarExamenpb(DeleteView):
    model=ExamenPerfilb
    template_name = 'app1/eliminar_examen.html'
    fields='__all__'
    success_url=reverse_lazy('app1:examenes')
    context_object_name = 'examen'


class ListaMedicamentos(ListView):
    model=Medicamento
    template_name = 'app1/lista_medicamentos.html'
    context_object_name = 'medicamento'

class AgregarMedicamento(CreateView):
    model=Medicamento
    template_name = 'app1/agregar_medicamento.html'
    fields='__all__'
    success_url= reverse_lazy('app1:lista_medicamentos')

class EditarMedicamento(UpdateView):
    model=Medicamento
    template_name = 'app1/editar_medicamento.html'
    fields='__all__'
    success_url=reverse_lazy('app1:lista_medicamentos')


class EliminarMedicamento(DeleteView):
    model=Medicamento
    template_name = 'app1/eliminar_medicamento.html'
    fields='__all__'
    success_url=reverse_lazy('app1:lista_medicamentos')
    context_object_name = 'medicamento'

    