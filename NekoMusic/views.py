from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from NekoMusic.models import playli,canciones
from .forms import Registro


from django.contrib.auth.models import User

# Create your views here.
'''
@login_required
def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin:index')
        else:
            return redirect('book_store_app:client_index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('book_store_app:client_index')

    form = LoginForm()
    return render(request, 'book_store_app/login.html', {'form': form})
'''
@login_required
def home(request):
    usuario = request.user
    idu=request.user.id
    li=playli.objects.all()
    PlayList=li.filter(ID_Usu=request.user)
    listaCan=canciones.objects.all()
    return render(request, "Home.html",{"lista":PlayList,"musica":listaCan})
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
def busqueda(request):
    li = playli.objects.all()
    listaCan = canciones.objects.all()
    if (request.GET["sound"]):
        search=request.GET["sound"]
        if len(search)>20:
            mensaje="texto demaciado largo"
            return render(request,"Busqueda.html",{"mesnaje":mensaje,"lista":li,"musica":listaCan})
        else:
            cancionSearch=canciones.objects.filter(nombre__icontains=search)
            return render(request,"Busqueda.html",{"can":cancionSearch,"query":search,"lista":li,"musica":listaCan})
    else:
        mensaje = "campo vacio"
        return render(request, "Busqueda.html", {"mesnaje": mensaje,"lista":li,"musica":listaCan})