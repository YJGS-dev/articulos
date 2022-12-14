"""src URL Configuration

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
from django.urls import path, include
from apps.articulo.views import articulo_screen_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articulo_screen_view, name = 'inicio'),

    #rest_framework
    path('api/articulo/', include('apps.articulo.api.urls','articulo_api')),
    path('api/departamento/', include('apps.departamento.api.urls','departamento_api')),
    path('api/clase/', include('apps.clase.api.urls','clase_api')),
    path('api/familia/', include('apps.familia.api.urls','familia_api')),
]
