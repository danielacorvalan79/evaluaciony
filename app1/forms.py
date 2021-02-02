from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core import validators
from .models import Administrador, Paciente, ExamenHemograma, ExamenPerfill, ExamenPerfilb, Medicamento
from django import forms
from django.conf import settings
import json



users = Paciente.objects.select_related('run').all().values_list('run', 'run')


class RegistroPaciente(forms.Form):

    run = forms.CharField(
        label='RUN',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'99.999.999-9'},
            ),
        validators=[validators.MaxLengthValidator(12,'Ingrese un Rut Válido!'),
                validators.MinLengthValidator(11,'Ingrese un Rut Válido!')]
        )
    nombre = forms.CharField(
        label='Nombre',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Nombre'})
        )
    apellido = forms.CharField(
        label='Apellido',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Apellido'})
        )



class LoginForm(forms.Form):

    user = forms.CharField(
        label = 'Usuario',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        })
    )

    password = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Contraseña'
        })
    )


class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Paciente
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'patologias': forms.TextInput(attrs={'class': 'form-control'}),
            }
        fields = ['nombre','apellido_paterno','fecha_nacimiento','email','direccion','telefono','patologias']

class PacientesForm(forms.ModelForm):
    class Meta:        
        model = Paciente
        
        fields = ['run']

        def __init__(self, *args, **kwargs):
            super(PacientesForm, self).__init__(*args, **kwargs)
            self.fields['run'] = forms.ModelChoiceField(
                queryset=Paciente.objects.select_related('run').all(),
                widget=forms.Select(attrs={'class': 'form-control'}))


class EditarDatosForm(forms.ModelForm):
    class Meta:
        model = Paciente
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'patologias': forms.TextInput(attrs={'class': 'form-control'}),
            }
        fields = ['nombre','apellido','fecha_nacimiento','edad','email','direccion','telefono','patologias']



class AgregarMedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        widgets = {
           'run': forms.Select(attrs={'class':'form-control'}),
           'fecha_indicacion': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
           'nombre': forms.TextInput(attrs={'class':'form-control'}),
           'hora': forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
           'dosis': forms.TextInput(attrs={'class':'form-control'})
        }
        fields = '__all__'


class PacientesFormSelect(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )


class ExamenHemogramaForm(forms.ModelForm):
    class Meta:
        model = ExamenHemograma
        widgets = {
                'run': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'hematocrito': forms.NumberInput(attrs={'class': 'form-control'}),
                'hemoglobina': forms.NumberInput(attrs={'class': 'form-control'}),
                }
        fields = '__all__'
        
class PerfillForm(forms.ModelForm):
    class Meta:
        model = ExamenPerfill
        widgets = {
                'run': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'colesterol_total': forms.NumberInput(attrs={'class': 'form-control'}),
                'trigliceridos': forms.NumberInput(attrs={'class': 'form-control'}),
                }
        fields = '__all__'

class PerfilbForm(forms.ModelForm):
    class Meta:
        model = ExamenPerfilb
        widgets = {
                'run': forms.Select(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
                'glucosa': forms.NumberInput(attrs={'class': 'form-control'}),
                'bilirrubina': forms.NumberInput(attrs={'class': 'form-control'}),
                }
        fields = '__all__'
        
        