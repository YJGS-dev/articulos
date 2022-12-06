from django.urls import path
from .views import api_list_clase_view

app_name = 'clase'

urlpatterns = [
    path("list/<int:pk>",api_list_clase_view, name = "list")
]