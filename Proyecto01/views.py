from datetime import datetime
from re import template
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context
import datetime 

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    nombre="Efrain"
    apellido="Diaz"
    temas=["Plantillas","Modelos","Formularios","Vistas","Deslpiegue"]
    p1=Persona("Profesor Efrain","Diaz")
    ahora=datetime.datetime.now()
    doc_externo=open(r"C:\Users\Steve\Desktop\Proyectos Django\Primer Proyecto\Proyecto01\Proyecto01\plantillas\plantilla01.html")
    pit=Template(doc_externo.read())
    doc_externo.close
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha_actual":ahora,"temas":temas})

    Document=pit.render(ctx)
    return HttpResponse(Document)

def getFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>Hola la hora es: %s </h1>
    </body>
    </html>"""%fecha_actual
    return HttpResponse(documento)

def getedad(request, edad,agnio):
    edadactual=25
    periodo=agnio-2022
    edadfutura=edad+periodo
    documento="""<html>
    <body>
    <h1>En el año %s tendras %s años </h1>
    </body>
    </html>"""%(agnio,edadfutura)
    return HttpResponse(documento)