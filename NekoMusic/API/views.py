from rest_framework.viewsets import ModelViewSet
from NekoMusic.models import canciones
from NekoMusic.API.serealizers import cancionesSerealizer

class cancionesAPIViews(ModelViewSet):#como se mostaran los datos
    serializer_class = cancionesSerealizer
    queryset = canciones.objects.all()