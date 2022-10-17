from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from NekoMusic.models import playli,canciones
# Create your views here.
@login_required
def home(request):
    li=playli.objects.all()
    return render(request, "Home.html",{"lista":li})
def salir(request):
    logout(request)
    return redirect('/')

