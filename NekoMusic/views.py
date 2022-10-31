from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from NekoMusic.models import playli,canciones,Tipos
from .forms import Registro
from django.contrib.auth.models import User,PermissionManager
from django.views import View
from .models import canciones
# Create your views here.
=======
from django.contrib.auth import logout
from NekoMusic.models import playli,canciones
# Create your views here.
@login_required
def home(request):

    li=playli.objects.all()
    listaCan=canciones.objects.all()
    return render(request, "Home.html",{"lista":li,"musica":listaCan})
def salir(request):
    logout(request)
    return redirect('/')

>>>>>>> parent of 99bf451 (sing up)
