from socket import fromshare
from django import forms


class FormularioBanco(forms.Form):

    nombre = forms.CharField()
    direccion = forms.CharField()
    tipoBco = forms.CharField()

class FormularioEmpleado(forms.Form):

    nombre = forms.CharField()
    legajo = forms.IntegerField()
    correo = forms.EmailField()

class FormularioServicio(forms.Form):

    nombre = forms.CharField()
    tipoServ = forms.CharField()

class FormularioSucursal(forms.Form):

    numero = forms.IntegerField()
    localidad = forms.CharField()
    horaApertura = forms.IntegerField()
    horaCierre = forms.IntegerField()
