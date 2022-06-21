from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from basedatos.models import producto

def inicio(request):
    return render(request, "index.html")

def seguimiento(request):
    return render(request, "seguimiento.html")

def donacion(request):
    return render(request, "donacion.html")

def carritoCompra(request):
    return render(request, "carritoCompra.html")

def productos(request):
    return render(request, "productos.html")

# para acceder a los parametros get se debe utilizar la siguiente sintaxis
def resultado(request):
#   mensaje = f'Se ha logeado el usuario {request.GET["correo"]}'
  llamadabd = producto.objects.filter(nombre__icontains="")
  contexto = {'datos':llamadabd}
  return render(request,"resultado.html",contexto)

# def inicio(request):
#     doc_externo = open("static/index.html") # este es el archivo que se renderizará (renderizar = interpretar lo que está en un texto, en este caso un html)
#     plt = Template(doc_externo.read())
#     doc_externo.close()
#     ctx = Context() # leng de ejecución sobre el que estoy corriendo mis plantillas
#     documento = plt.render(ctx)
#     return HttpResponse(documento) # -> ahora tenemos archivo html enriquecido que reconoce python (o algo así)

# def seguimiento(request):
#     doc_externo = open("static/seguimiento.html")
#     plt = Template(doc_externo.read())
#     doc_externo.close()
#     ctx = Context(
#         {"producto":"Macetero cerámica con plato",
#         "lista":["$6.570", "elemento2", "elemento3"]}
#         )
#     documento = plt.render(ctx)
#     return HttpResponse(documento)

# def donacion(request):
#     doc_externo = open("static/donacion.html")
#     plt = Template(doc_externo.read())
#     doc_externo.close()
#     ctx = Context()
#     documento = plt.render(ctx)
#     return HttpResponse(documento)

# def carritoCompra(request):
#     doc_externo = open("static/carritoCompra.html")
#     plt = Template(doc_externo.read())
#     doc_externo.close()
#     ctx = Context()
#     documento = plt.render(ctx)
#     return HttpResponse(documento)

# def productos(request):
#     doc_externo = open("static/productos.html")
#     plt = Template(doc_externo.read())
#     doc_externo.close()
#     ctx = Context()
#     documento = plt.render(ctx)
#     return HttpResponse(documento)