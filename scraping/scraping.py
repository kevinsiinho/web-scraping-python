#importando librerias
import requests
from bs4 import BeautifulSoup
#convierte el archivo en un

def Run(url,clase):
    ####aqui empieza el scraping
    datos=[]
    pagina= requests.get(url)
    #leyendo la información guardada en page
    soup = BeautifulSoup(pagina.content,'html.parser')
    #buscando las etiquetas que quiero 
    info = soup.find_all(class_=clase)
    lineas = info[0].text.split("\n")
    datos.extend(lineas)
    datos=[linea for linea in lineas if len(linea.strip()) > 0]
    for x,i in enumerate(datos):
        caracter = "."
        caracteres = i[:5]
        if caracter in caracteres: #devuelve un true
            datos[x]=i.split(caracter, 1)[-1].strip()
        
    return datos  

