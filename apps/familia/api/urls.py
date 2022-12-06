from django.urls import path
from .views import api_list_familia_view

app_name = 'familia'

urlpatterns = [
    path("list/<int:pk>",api_list_familia_view, name = "list")
]