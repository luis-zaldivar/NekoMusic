from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tipos(models.Model):
    User=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    TipoUser=models.CharField(max_length=10)
    TiempoSus=models.IntegerField()
    def __str__(self):
        return '%s'%(self.TipoUser)

class canciones(models.Model):
    nombre=models.CharField(max_length=40)
    autor=models.CharField(max_length=40)
    album=models.CharField(max_length=40)
    dircan=models.FileField(upload_to='Canciones/')
    genero=models.CharField(max_length=30)

    def delete(self,*args,**kwargs):
        self.dircan.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return '%s'%(self.nombre)

class playli(models.Model):
    NomPlay = models.CharField(max_length=30)
    ID_Can = models.ManyToManyField(canciones)
    ID_Usu = models.ManyToManyField(User)
    def __str__(self):
        return '%s' % (self.NomPlay)
