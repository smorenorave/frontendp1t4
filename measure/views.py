import requests
from django.shortcuts import render, HttpResponse
# Create your views here.
def measure(request):
    if 'codigo' and 'latitud' and 'longitud' and 'terreno' in request.GET and 'area' in request.GET:
        codigo = request.GET['codigo']
        latitud = request.GET['latitud']
        longitud = request.GET['longitud']
        terreno = request.GET['terreno']
        area = request.GET['area']

        # Verifica si el value no esta vacio
        if codigo:
            if int(area) >= 0:
                # Crea el json para realizar la petición POST al Web Service
                args = {'codigo':str(codigo), 'latitud': int(latitud), 'longitud': int(longitud), 'area':int(area), 'terreno':str(terreno)}
                print(args)
                response = requests.post('http://127.0.0.1:8000/measure/', args)
                # Convierte la respuesta en JSON
                measure_json = response.json()
    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measure/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})