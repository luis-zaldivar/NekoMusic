from rest_framework.serializers import ModelSerializer
from NekoMusic.models import canciones,playli
from django.contrib.auth.models import User

class cancionesSerealizer(ModelSerializer):
    class Meta:
        model = canciones
        fields=['id','nombre','autor','album','dircan','genero']#datos que se mostraran en la api
class PlaylistSerealizer(ModelSerializer):
    class Meta:
        model = playli
        fields=['NomPlay','ID_Can','ID_Usu']

class userSerealizer(ModelSerializer):
    class Meta:
        model= User
        fields=['username']
