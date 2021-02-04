from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views import generic
from .models import Paciente, Examen, Medicamento
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def home(request):
    return render(request, 'app1/main.html') 

def registro(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('app1:home') 

    else:
        f = UserCreationForm()

    return render(request, 'app1/registro.html', {'form': f})  

def exams(request):
    return render(request, 'app1/examenes.html') 

def meds(request):
    return render(request, 'app1/medicamento.html')

def cal(request):
    return render( request, 'app1/calendario.html')

lista=[]
class PacientePersonalizado(View):
    def get(self, request, pk):
        resultado = list(Examen.objects.values().all())
        for elemento in resultado:
            resultado=elemento.get('resultado')
            lista.append(resultado)
            lista_paciente =list(Paciente.objects.filter(run=pk).values())
            context = {'paciente': lista, 'run':pk, 'lista':lista}
            return render(request, 'app1/paciente_per.html', context=context)

class CrearPaciente(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=Paciente
    template_name = 'app1/crear_paciente.html'
    fields='__all__'
    success_url= reverse_lazy('app1:lista')
    login_url='app1:lista'

    def test_func(self):
        return usuario(self.request.user)

class AgregarPaciente(CreateView):
    model=Paciente
    template_name = 'app1/agregar_paciente.html'
    fields='__all__'
    success_url= reverse_lazy('app1:lista')

class Inicio(generic.TemplateView):
    template_name = 'app1/index.html'


class ListaPaciente(ListView):
    model=Paciente
    template_name = 'app1/lista_paciente.html'
    context_object_name = 'paciente'


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

class ListaExamenes(ListView):
    model=Examen
    template_name = 'app1/examenes.html'
    context_object_name = 'examen'

class AgregarExamen(CreateView):
    model=Examen
    template_name = 'app1/agregar_examen.html'
    fields='__all__'
    success_url= reverse_lazy('app1:examenes')

class EliminarExamen(DeleteView):
    model=Examen
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

class inicio1(LoginRequiredMixin, View):
    def get (self, request):
        return render (request, 'app1/main.html')