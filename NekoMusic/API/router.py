from rest_framework.routers import DefaultRouter
from NekoMusic.API.views import cancionesAPIViews,PlayListAPIViews,userAPIViews

router_Musica=DefaultRouter()

router_Musica.register(prefix='canciones',basename='cancionesget',viewset=cancionesAPIViews)#como se accede a la informacion de la api
router_Musica.register(prefix='playlistget',basename='playlistget',viewset=PlayListAPIViews)
router_Musica.register(prefix='Usuarios',basename='Usuariosget',viewset=userAPIViews)