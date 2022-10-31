from rest_framework.routers import DefaultRouter
from NekoMusic.API.views import cancionesAPIViews

router_Musica=DefaultRouter()

router_Musica.register(prefix='cancionesget',basename='cancionesget',viewset=cancionesAPIViews)#como se accede a la informacion de la api