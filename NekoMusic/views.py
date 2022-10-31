from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from NekoMusic.models import playli,canciones,Tipos
from .forms import Registro
from django.contrib.auth.models import User,PermissionManager
from django.views import View
from .models import canciones
# Create your views here.
