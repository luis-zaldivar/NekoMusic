from django.contrib import admin
from NekoMusic.models import canciones,Tipos,playli
# Register your models here.

class cancionesTabla(admin.ModelAdmin):
    list_display = ("nombre","autor","genero")

class usuariosTabla(admin.ModelAdmin):
    list_display = ("TipoUser","TiempoSus")



admin.site.register(canciones,cancionesTabla)
admin.site.register(Tipos,usuariosTabla)
admin.site.register(playli)