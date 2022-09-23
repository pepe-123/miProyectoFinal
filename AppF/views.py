from ast import Pass
import email
from django.shortcuts import render
from AppF.models import *
from AppF.forms import FormularioBanco, FormularioEmpleado, FormularioServicio, FormularioSucursal
from django.http import HttpResponse

# from ProyectoF.AppF.forms import FormularioServicio, FormularioSucursal

# Create your views here.
def inicio(request):
    
    return render(request, "AppF/inicio.html")

def banco(request):

    """
    bco = Banco(nombre="Santander", direccion="Espora 123", tipoBco="Privado")

    bco.save()
    """

    return render(request, "AppF/bancos.html")

def empleado(request):
    
    return render(request, "AppF/empleados.html")

def servicio(request):
    
    return render(request, "AppF/servicios.html")

def sucursal(request):
    
    return render(request, "AppF/sucursales.html")

def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioBanco(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            bcoF = Banco(nombre=info["nombre"], direccion=info["direccion"], tipoBco=info["tipoBco"])

            bcoF.save()

            return render(request, "AppF/inicio.html")

    else:

        formulario1 = FormularioBanco()

    return render(request, "AppF/form1.html", {"form1":formulario1})

def formulario2(request):

    if request.method=="POST":

        formulario2 = FormularioEmpleado(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            empF = Empleado(nombre=info["nombre"], legajo=info["legajo"], correo=info["correo"])

            empF.save()

            return render(request, "AppF/inicio.html")

    else:

        formulario2 = FormularioEmpleado()

    return render(request, "AppF/form2.html", {"form2":formulario2})

def formulario3(request):

    if request.method=="POST":

        formulario3 = FormularioServicio(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            servF = Servicio(nombre=info["nombre"], tipoServ=info["tipoServ"])

            servF.save()

            return render(request, "AppF/inicio.html")

    else:

        formulario3 = FormularioServicio()

    return render(request, "AppF/form3.html", {"form3":formulario3})

def formulario4(request):

    if request.method=="POST":

        formulario4 = FormularioSucursal(request.POST)

        if formulario4.is_valid():

            info = formulario4.cleaned_data

            sucF = Sucursal(numero=info["numero"], localidad=info["localidad"], horaApertura=info["horaApertura"], horaCierre=info["horaCierre"])

            sucF.save()

            return render(request, "AppF/inicio.html")

    else:

        formulario4 = FormularioSucursal()

    return render(request, "AppF/form4.html", {"form4":formulario4})

def busquedaBancos(request):

    return render(request, "AppF/busquedaBancos.html")

def buscar(request):

    if request.GET["tipo"]:

        busqueda = request.GET["tipo"]
        bancos = Banco.objects.filter(tipoBco__icontains=busqueda)

        return render(request, "AppF/inicio.html", {"bancos":bancos, "busqueda":busqueda})
    
    else:

        mensaje = "No se encontraron datos."

    return HttpResponse(mensaje)

