from django.urls import path
from .views import (
    api_detalle_articulo_view,
    api_crear_articulo_view,
    api_update_articulo_view,
    api_eliminar_articulo_view
)

app_name = 'articulo'

urlpatterns = [
    path("<int:sku>",api_detalle_articulo_view, name = "detalle"),
    path("create", api_crear_articulo_view, name = "create"),
    path("update", api_update_articulo_view, name = "update"),
    path("<int:sku>/delete", api_eliminar_articulo_view, name = "delete")
]