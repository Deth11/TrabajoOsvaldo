"""plantas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from plantasapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cargaDatos/', views.cargar_datos, name='cargaComprador'),
    path('listarPedidosNecesarios/', views.listar_pedidos_necesarios, name='listaNecesarios'),
    path('listarPedidosRepartir/', views.listar_pedidos_repartir, name='listaRepartir'),
    path('listarPedidosCargar/', views.listar_pedidos_cargar, name='listaCargar'),
]
