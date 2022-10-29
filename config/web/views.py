from django.shortcuts import render

# Create your views here.
#Cada vista es una funcion de python 

def Home(request):
    return render(request, 'index.html')
