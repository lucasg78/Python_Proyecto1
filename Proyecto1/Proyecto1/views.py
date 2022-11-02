from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def vista_saludo(request):
    return HttpResponse("Hola Mundo")


def iniciar_sesion(request):
    return HttpResponse("""
                        <h1>Pasame tu username y password</h1>
                        <p style="color:red">Esto es una prueba</p>
                        """)


def dia_hoy(request, nombre):
    hoy = datetime.now()
    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)


def anio_nacimiento(request, edad):
    edad = int(edad)
    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en el año {anio_nac}")


def vista_plantilla(request):
    # Abrimos el archivo
    archivo = open(r"G:\Mi unidad\Formación\Programación\Python\Coderhouse\clases\clase17 26102022\PythonProyecto1\Proyecto1\Proyecto1\templates\template1.html")
    
    # Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())
    
    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {
    "fecha": datetime.now().strftime("%d/%m/%Y"),
    "nombre": "Lucas",
    "apellido": "Gallo",
    "edad": 44,
    "email": "lucasgallo@gmail.com",
    }
    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
    
    # Retornamos la respuesta
    return HttpResponse(documento)
