from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados

# Create your views here.
#Cada vista es una funcion de python 

def Home(request):
    return render(request, 'index.html')

def Platos(request):
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

    return render(request, 'platos.html', diccionarioEnvioDatos)

def Empleados(request):

    formularioEmpleados = FormularioRegistroEmpleados()

    diccionarioEnvioDatosEmpleados={
        'formEmpleados': formularioEmpleados
    }

    if request.method == 'POST':
        datosFormulario = FormularioRegistroEmpleados(request.POST)
        
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data

    return render(request, 'empleados.html', diccionarioEnvioDatosEmpleados)
