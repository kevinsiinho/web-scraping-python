from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Link,Frase
from  scraping.scraping import Run
# Create your views here.

def inicio(request):
    return  HttpResponse("<h1>Hola mundo</h1>")
def index(request):
    return render(request,'paginas/index.html')#accede automaticamente a la carpeta templates
def create(request):
    return render(request, 'crud/create.html')

def urls(request):
    links=Link.objects.all()
    global datos
    datos=None
    return render(request, 'crud/urls.html',{"links":links})


datos=None

def frases(request,id):
    global datos
    if not datos:
        link=Link.objects.get(id=id)
        url=link.url
        clase=link.clase
        estado=Link.estado
        print(link,clase)
        datos=Run(url,clase)
    else:
        link = Link.objects.get(id=id)
        estado = link.estado    
    
    if request.method == 'POST': 
        if "delete" in request.POST: 
            i = request.POST.get('delete')
            datos.remove(i)
        if request.POST.get('submit_button')=="guardar":
            if estado=="Pendiente":
                idlink = Link.objects.get(pk=id)
                link.estado="Realizado"
                link.save()
                for texto in datos:
                    frase = Frase(texto=texto, idlink=idlink)
                    frase.save()
                    datos=None
            else:
                return HttpResponse("<h1>Ya haz hecho escraping a este sitio web</h1>")
      
    return render(request, 'crud/frases.html',{"info":datos,"id":id,"estado":link.estado})

def comentarios(request):
    return render(request, 'crud/comentario.html')