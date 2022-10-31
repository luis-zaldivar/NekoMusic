from rest_framework.serializers import ModelSerializer
from NekoMusic.models import canciones

class cancionesSerealizer(ModelSerializer):
    class Meta:
        model = canciones
        fields=['nombre','autor','album','dircan','genero']#datos que se mostraran en la api
