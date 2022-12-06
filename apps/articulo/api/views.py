from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection


@api_view(['GET', ])
def api_detalle_articulo_view(request, sku):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT get_articulo(%s)", [sku])
            articulo = cursor.fetchone()
            if not articulo[0]:
                return Response({'message': 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        return Response({'message': 'success','data':articulo[0]}, status = status.HTTP_200_OK)

@api_view(['POST', ])
def api_crear_articulo_view(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT get_articulo(%s)", [request.POST.get("sku")])
            articulo = cursor.fetchone()
            if articulo[0]:
                return Response({'message': 'Ya existe un artículo con ese sku'}, status = status.HTTP_400_BAD_REQUEST)
            values = [
                request.POST.get("sku"),
                request.POST.get("nombre"),
                request.POST.get("marca"),
                request.POST.get("modelo"),
                request.POST.get("cantidad"),
                request.POST.get("stock"),
                request.POST.get("departamento"),
                request.POST.get("clase"),
                request.POST.get("familia")
            ]
            cursor.execute("""SELECT create_articulo(
                %s::smallint, 
                %s::varchar, 
                %s::varchar, 
                %s::varchar, 
                %s::smallint, 
                %s::smallint, 
                %s::bigint, 
                %s::bigint, 
                %s::bigint)
            """, values)
            cursor.fetchone()
        return Response({'message': 'Artículo agregado exitosamente'}, status = status.HTTP_200_OK)

@api_view(['PUT', ])
def api_update_articulo_view(request):
    if request.method == 'PUT':
        values = [
            request.POST.get("sku"),
            request.POST.get("nombre"),
            request.POST.get("marca"),
            request.POST.get("modelo"),
            request.POST.get("cantidad"),
            request.POST.get("stock"),
            request.POST.get("departamento"),
            request.POST.get("clase"),
            request.POST.get("familia"),
            request.POST.get("descontinuado"),
        ]
        print(values)
        with connection.cursor() as cursor:
            cursor.execute("""SELECT update_articulo(
                %s::smallint, 
                %s::varchar, 
                %s::varchar, 
                %s::varchar, 
                %s::smallint, 
                %s::smallint, 
                %s::bigint, 
                %s::bigint, 
                %s::bigint, 
                %s::smallint)
            """, values)
            cursor.fetchone()
        return Response({'message': 'Artículo actualizado exitosamente'}, status = status.HTTP_200_OK)

@api_view(['DELETE', ])
def api_eliminar_articulo_view(request, sku):
    if request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("""SELECT delete_articulo(%s::smallint)""", [sku])
            cursor.fetchone()
        return Response({'message': 'Artículo eliminado'}, status = status.HTTP_200_OK)


