from django import forms
from .models import Empresas

class CreateUnitMeasurement(forms.Form):
    codigo = forms.CharField(max_length=3, label='CÓDIGO')
    nombre = forms.CharField(max_length=50, label='UNIDAD DE MEDIDA')

class CreateCompany(forms.Form):
    rut = forms.CharField(max_length=8,label='RUT')
    dvRut = forms.CharField(max_length=1)
    razSoc = forms.CharField(max_length=150,label='RAZÓN SOCIAL')
    nomFant = forms.CharField(max_length=150,label='NOMBRE FANTASÍA')
    codigo = forms.CharField(max_length=5,label='CÓDIGO')
    giro = forms.CharField(max_length=150,label='GIRO')
