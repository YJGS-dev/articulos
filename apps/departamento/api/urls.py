from django.urls import path
from .views import api_list_departamento_view

app_name = 'departamento'

urlpatterns = [
    path("list",api_list_departamento_view, name = "list")
]