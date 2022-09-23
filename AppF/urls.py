from django.urls import path
from AppF.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("bancos/", banco, name="Bancos"),
    path("empleados/", empleado),
    path("servicios/", servicio, name="Servicios"),
    path("sucursales/", sucursal, name="Sucursales"),
    path("form1/", formulario1),
    path("form2/", formulario2),
    path("form3/", formulario3),
    path("form4/", formulario4),
    path("buscarBancos/", busquedaBancos),
    path("buscar/", buscar),
]