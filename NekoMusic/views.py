from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from NekoMusic.models import playli,canciones
from .forms import Registro

from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    persona=0
    li=playli.objects.all()
    listaCan=canciones.objects.all()
    return render(request, "Home.html",{"lista":li,"musica":listaCan})
def salir(request):
    logout(request)
    return redirect('/')
def Sign_up(request):
    data={
        'form':Registro
    }
    if request.method=='POST':
        formulario=Registro(data=request.POST)
        if formulario.is_valid():
            formulario.save();
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Registro exitoso")
            return redirect(to="/")
        data["form"]=formulario
    return render(request,'registration/registro.html',data)
