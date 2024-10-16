from django.http import HttpResponse
from django.template import Template, Context
from datetime import *

#Creamos una vista con Django --> PRimera vista
def saludos(request):

    doc_ext = open("C:/Users/Pampa/Desktop/Tecnicatura En Programacion/2024/16 - SegundoSemestre/Curso de Pildoras informaticas Django/curso_django_gallego_pildoras/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    documento = plt.render(ctx)

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