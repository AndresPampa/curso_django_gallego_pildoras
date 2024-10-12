from django.http import HttpResponse
from datetime import *

#Creamos una vista con Django --> PRimera vista
def saludos(request):
    documento = """<html><body>
                   <h1>Hola Alumnos esta es nuestra primera pagina con Django</h1>
                   </body></html>"""
    return HttpResponse(f"{documento}")

def despedida(request):
    return HttpResponse("Hasta luego reyes")



def dame_fecha(request):

    fecha_actual = datetime.now()

    documento = f"""<html><body>
                   <h1>Fecha y Hora Actual: {fecha_actual}</h1>
                   </body></html>"""
    return HttpResponse(documento)


def calculaEdad(request, anio, edad):

    # edadActual = edad
    periodo = anio - 2024
    edadFutura = edad + periodo

    documento = f"""<html><body>
                   <h1>En el año: {anio} tendras: {edadFutura}</h1>
                   </body></html>"""
    
    return HttpResponse(documento)