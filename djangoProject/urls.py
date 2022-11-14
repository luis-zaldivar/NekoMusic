"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from NekoMusic import views
from django.conf import settings
from django.views.static import serve
from NekoMusic.API.router import router_Musica

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router_Musica.urls)),
    path("", views.home, name="Home"),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('login/',views.login_view,name="login"),
    path('salir/', views.salir, name='salir'),
    path('Sign_up/', views.Sign_up, name='Sign_up'),
    path("buscarx/", views.busqueda),
    path("NewList/", views.nuevaLista),
    path("MosPlay/", views.mostrarPlayList),
    path("Agregar/", views.AgregarLista),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns += {
    re_path(r'^Multimedia/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
}
