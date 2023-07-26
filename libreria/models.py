from django.db import models


class Frase(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField(null=True)
    like = models.IntegerField(null=False,default=0)
    idlink = models.ForeignKey('Link' , models.DO_NOTHING, db_column='idlink')  # Field name made lowercase.
    
    def __str__(self):
        frases="Frase: "+self.texto+" - Like: "+str(self.like) 
        return frases
    
    def eliminar_frase(self):
        # Método para eliminar la frase
        self.delete()
    
class Link(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    url = models.TextField(max_length=200,null=True)
    clase = models.CharField(max_length=60, null=True)
    tipoid = models.ForeignKey('Tipo' , models.DO_NOTHING, db_column='tipoid')
    estado = models.CharField(max_length=45, null=False,default="Pendiente")
    def __str__(self):
        links="Url: "+self.url+" - Tipo: "+str(self.tipoid)+" - Estado: "+self.estado 
        return links
   
class Tipo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(verbose_name="nombre", max_length=45, null=True)
    def __str__(self):
        tipo=self.nombre
        return tipo
    
class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    texto = models.TextField(max_length=200,null=True)
    date = models.DateField(verbose_name="Fecha" , null=True)
