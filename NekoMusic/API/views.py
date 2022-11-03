from rest_framework.viewsets import ModelViewSet
from NekoMusic.models import canciones,playli
from django.contrib.auth.models import User
from NekoMusic.API.serealizers import cancionesSerealizer,PlaylistSerealizer,userSerealizer

class cancionesAPIViews(ModelViewSet):#como se mostaran los datos
    serializer_class = cancionesSerealizer
    queryset = canciones.objects.all()
class PlayListAPIViews(ModelViewSet):#como se mostaran los datos
    serializer_class = PlaylistSerealizer
    queryset = playli.objects.all()
class userAPIViews(ModelViewSet):
    serializer_class =userSerealizer
    queryset = User.objects.all()
