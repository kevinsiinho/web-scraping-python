from django.contrib import admin
from .models import Link
from .models import Frase
from .models import Tipo

# Register your models here.
admin.site.register(Link)
admin.site.register(Frase)
admin.site.register(Tipo)