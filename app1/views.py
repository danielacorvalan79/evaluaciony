from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic import ListView, View
from django.views import generic
from .models import Administrador, Usuarios, Paciente, ExamenHemograma, ExamenPerfill, ExamenPerfilb, Medicamento
from .forms import RegistroPaciente, LoginForm, EditarUsuarioForm, PacientesForm, EditarDatosForm, AgregarMedicamentoForm
from .forms import ExamenHemogramaForm, PerfillForm, PerfilbForm 
from .forms import PacientesFormSelect
from django.urls import reverse_lazy 
from django.contrib import messages
from django.conf import settings
import json


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


    def get(self, request):
        context = {'seleccionar': self.select_form}
        return render(request, 'app1/examenes.html', context)
       
    def post(self, request):
        run = request.POST['pacientes']
        hemograma = list(ExamenHemograma.objects.select_related('run').\
            filter(run=run).values())
        perfil_lipidico = list(ExamenPerfill.objects.select_related('run').\
            filter(run=run).values())
        perfil_bioquimico = list(ExamenPerfilb.objects.select_related('run').\
            filter(run=run).values())
        context = {
                "seleccionar":self.select_form,
                "hemograma":hemograma,
                "perfil_lipidico":perfil_lipidico,
                "perfil_bioquimico":perfil_bioquimico,
                "grafico_hemograma": self.get_datos_hemograma(run),
                "grafico_perfil_lipidico": self.get_datos_perfil_lipidico(run),
                "grafico_perfilbioquimico": self.get_datos_perfil_bioquimico(run),
                }
        return render(request, 'app1/examenes.html', context)

    def get_datos_examenhemograma(self, run):
        hemograma = ExamenHemograma.objects.select_related('run').\
            filter(run=run).\
                values('fecha','hemoglobina','hematocrito')
        grafico_hemograma = {
            'fecha':[ str(dato['fecha']) for dato in hemograma],
            'hemoglobina':[ float(dato['hemoglobina']) for dato in hemograma],
            'hematocrito':[ float(dato['hematocrito']) for dato in hemograma],
        } 
        return grafico_hemograma
    
    def get_datos_perfill(self, run):
        perfil_lipidico = ExamenPerfill.objects.select_related('run').\
            filter(run=run).\
                values('fecha','colesterol_total','trigliceridos')
        grafico_perfill = {
            'fecha':[ str(dato['fecha']) for dato in perfil_lipidico],
            'colesterol_total':[ float(dato['colesterol_total']) for dato in perfil_lipidico],
            'trigliceridos':[ float(dato['trigliceridos']) for dato in perfil_lipidico],
        } 
        return grafico_perfill

    def get_datos_perfilb(self, run):

        perfil_bioquimico = ExamenPerfilb.objects.select_related('run').\
            filter(id_usuario=run).\
                values('fecha','glucosa','bilirrubina')
        grafico_perfilb = {
            'fecha':[ str(dato['fecha']) for dato in perfil_bioquimico],
            'glucosa':[ float(dato['glucosa']) for dato in perfil_bioquimico],
            'bilirrubina_total':[ float(dato['bilirrubina_total']) for dato in perfil_bioquimico],
        } 
        return grafico_perfilb

class AgregarHemograma(CreateView):
    model = ExamenHemograma
    form_class = ExamenHemogramaForm
    template_name = 'app1/agregar_hemograma.html'
    success_url = reverse_lazy('app1:examenes')


class AgregarPerfill(CreateView):
    model = ExamenPerfill
    form_class = PerfillForm
    template_name = 'app1/agregar_perfill.html'
    success_url = reverse_lazy('app1:examenes')
    
class AgregarPerfilb(CreateView):
    model = ExamenPerfilb
    form_class = PerfilbForm
    template_name = 'app1/agregar_perfilb.html'
    success_url = reverse_lazy('app1:examenes')
    


class ListaExamenesH(ListView):
    model=ExamenHemograma
    template_name = 'app1/examenes.html'
    context_object_name = 'examenes'

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
    context_object_name = 'examenes'

class ListaExamenespl(ListView):
    model=ExamenPerfill
    template_name = 'app1/examenes.html'
    context_object_name = 'examenes'

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
    context_object_name = 'examenes'

class ListaExamenespb(ListView):
    model=ExamenPerfilb
    template_name = 'app1/examenes.html'
    context_object_name = 'examenes'

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
    context_object_name = 'examenes'


class ListaMedicamentos(ListView):
    model=Medicamento
    template_name = 'app1/lista_medicamentos.html'
    context_object_name = 'medicamentos'

class AgregarMedicamentos(CreateView):
    model=Medicamento
    template_name = 'app1/agregar_medicamentos.html'
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




class Home(ListView):
    model = Paciente
    form_class = PacientesForm
    template_name = 'app1/home.html'
    context_object_name = 'pacientes'
    success_url = 'app1:Home'

    
    def get(self, request, **kwargs):
        pacientes = self.form_class
        #print(DatosPersonales.objects.select_related('id_usuario').all().values_list('id_usuario', 'id_usuario'))
        context = {'pacientes':pacientes}
        return render(request, self.template_name, context)  


    def post(self, request):
        run = request.POST['run'] 
        datos_paciente = Paciente.objects.filter(id_usuario=run).values()[0]
        pacientes = self.form_class
        context = {'pacientes':pacientes, 
            'datos_paciente': datos_paciente,
            'id':datos_paciente['run']
            }
        return render(request, 'app1/home.html', context)


class EditarDatosPersonales(View):
    model = Paciente
    form_class = EditarDatosForm
    template_name = 'app1/edit.html'
    success_url = 'app1:Home'

    def get(self, request, pk):
        #print(pk)
        datos_paciente = self.model.objects.filter(id=pk).values()[0]
        #print(datos_paciente)
        formulario = self.form_class(initial=datos_paciente)
        #print(formulario)
        context = {'form': formulario, 'run':pk}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        print(pk)
        formulario = self.form_class(request.POST) 
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            print(form_data)
            self.model.objects.filter(run=pk).update(
                            nombre = form_data['nombre'],
                            apellido = form_data['apellido'],
                            fecha_nacimiento = form_data['fecha_nacimiento'],
                            direccion = form_data['direccion'],
                            email = form_data['email'],
                            telefono = form_data['telefono'],
                            patologias = form_data['patologias']
                            )
            return redirect(self.success_url)
        else:
            print('inválido')
            return render(request, self.template_name, {'form': formulario}) 

class MedicamentoView(View):
    template_name = 'app1/medicamento.html'
    form_class = PacientesForm
    success_url = 'app1:medicamento'

    def get(self, request):
        pacientes = self.form_class
        context = {'pacientes':pacientes}
        return render (request, self.template_name, context)
    
    def post(self, request):
        run = request.POST['pacientes']
        paciente = Medicamento.objects.filter(id_usuario = run).values()
        pacientes = self.form_class
        context = {'pacientes':pacientes, 'datos': paciente}
        return render(request, self.template_name, context)


class AgregarMedicamento(CreateView):
    model = Medicamento
    form_class = AgregarForm
    template_name = 'app1/agregar_medicamento.html'
    success_url = reverse_lazy('app1:medicamentos')   