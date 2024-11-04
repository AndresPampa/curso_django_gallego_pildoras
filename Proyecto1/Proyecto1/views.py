from django.http import HttpResponse
from django.template import Template, Context
from datetime import *
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#Creamos una vista con Django --> PRimera vista
def saludos(request):

    p1 = Persona("Profesor Juan", "Diaz")
    # nombre = "Juan"
    # apellido = "Diaz"
    now = datetime.now()

    temas_del_curso = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']

    # doc_ext = open("C:/Users/Pampa/Desktop/Tecnicatura En Programacion/2024/16 - SegundoSemestre/Curso de Pildoras informaticas Django/curso_django_gallego_pildoras/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")
    # doc_ext.close()

    # doc_ext = loader.get_template('mi_plantilla.html')

    # plt = Template(doc_ext.read())
    # ctx = Context({"nombre_persona": p1.nombre, 
    #                "apellido_persona": p1.apellido, 
    #                "Hora": now, 
    #                "temas": temas_del_curso})#el contexto admite diccionarios
    # documento = plt.render(ctx)
    
    # documento = doc_ext.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "Hora": now, "temas": temas_del_curso})

    return render(request, "mi_plantilla.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "Hora": now, "temas": temas_del_curso})

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



def cursoC(request):
    fecha_actual = datetime.now()
    return render(request, "cursoC.html", {"dameFecha": fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.now()
    return render(request, "cursoCss.html", {"dameFecha": fecha_actual})