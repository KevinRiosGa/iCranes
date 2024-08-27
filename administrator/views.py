from django.shortcuts import render,redirect,HttpResponse
from .models import UnidadMedida,Empresas
from .forms import CreateUnitMeasurement,CreateCompany


# Create your views here.

def createUnitMeasurement(request):
    if request.method == 'POST':
        form = CreateUnitMeasurement(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            nombre = form.cleaned_data['nombre'].upper()
            item = UnidadMedida(codigo=codigo,nombre=nombre)
            item.save()
            return redirect('createUnitMeasurement')
    else:
        form = CreateUnitMeasurement()
    return render(request,'createUnitMeasurement.html', {'form':form})

def createCompany(request):
    if request.method == 'POST':
        form = CreateCompany(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut'].upper()
            dvRut = form.cleaned_data['dvRut'].upper()
            razSoc = form.cleaned_data['razSoc'].upper()
            nomFant = form.cleaned_data['nomFant'].upper()
            giro = form.cleaned_data['giro'].upper()
            codigo = form.cleaned_data['codigo'].upper()
            item = Empresas(rut=rut,dvRut=dvRut,razSoc=razSoc,nomFant=nomFant,giro=giro,codigo=codigo)
            item.save()
            return redirect('createCompany')
    else:
        form = CreateCompany()
    return render(request,'createCompany.html',{'form':form})