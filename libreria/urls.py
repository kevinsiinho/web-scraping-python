from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("registro",views.create,name="create"),
    path("urls",views.urls,name="urls"),
    path("frases/<int:id>",views.frases,name="frases"),
    path("frases",views.frases,name="frases"),
    path("comentario",views.comentarios,name="comentarios"),
]