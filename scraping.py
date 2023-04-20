#importando librerias
import requests
from bs4 import BeautifulSoup
import json
#Haciendo la peticón para extraer el html y se pone la página que quiero hacer el scraping

with open("sitios.json") as sitio:
    #convierte el archivo en un json
    sitio_json=json.load(sitio)
    for sitio in sitio_json["sitios"]:
        url=sitio["url"]
        clase=sitio["clase"]

        ####aqui empieza el scraping
        pagina= requests.get(url)
        #leyendo la información guardada en page
        soup = BeautifulSoup(pagina.content,'html.parser')
        #buscando las etiquetas que quiero 
        info = soup.find_all(class_=clase)
        #recorriendo las etiquetas
        for i in info:
            informacion=i.text
            print("-------------------------")

        print(informacion)   
 
