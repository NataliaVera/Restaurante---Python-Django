from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
from web.models import Platos, Empleados

# Create your views here.
#Cada vista es una funcion de python 

def Home(request):
    return render(request, 'index.html')

def PlatosVista(request):
    #cargar el formulario de registros de platos 
    formulario = FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia al template 
    diccionarioEnvioDatos ={
        'formulario':formulario
    }

    #RECIBIENDO DATOS DEL FORMULARIO 
    #PETICION POST 
    if request.method == 'POST':
        datosFormulario = FormularioRegistroPlatos(request.POST)
        
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            #Enviando datos a la DB
            platoNuevo=Platos(
                nombre= datosLimpios["nombrePlato"], 
                descripcion=datosLimpios["descripcionPlato"], 
                imagen=datosLimpios["fotoPlato"], 
                precio=datosLimpios["precioPlato"],
                categoria=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()
            

    return render(request, 'platos.html', diccionarioEnvioDatos)

def EmpleadosVista(request):

    formularioEmpleados = FormularioRegistroEmpleados()

    diccionarioEnvioDatosEmpleados={
        'formEmpleados': formularioEmpleados
    }

    if request.method == 'POST':
        datosFormulario = FormularioRegistroEmpleados(request.POST)
        
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            empleadoNuevo= Empleados(
                nombre= datosLimpios["nombreEmpleado"],
                apellido=datosLimpios["apellidoEmpleado"], 
                telefono=datosLimpios["telefonoEmpleado"], 
                cargo=datosLimpios["cargoEmpleado"]
            )
            empleadoNuevo.save()

    return render(request, 'empleados.html', diccionarioEnvioDatosEmpleados)
