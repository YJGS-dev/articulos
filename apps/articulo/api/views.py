from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection


@api_view(['GET', ])
def api_detalle_articulo_view(request, sku):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = cursor.execute("SELECT get_articulo(%s)", [sku])
            query = cursor.fetchone()
            if not query[0]:
                return Response({'mesagge': 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        return Response({'message': 'success','data':query[0]})

@api_view(['POST', ])
def api_crear_articulo_view(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
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
            articulo = cursor.execute("""SELECT create_articulo(
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
            articulo = cursor.fetchone()
        return Response({'message': 'data'})

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
            articulo = cursor.execute("""SELECT update_articulo(
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
            articulo = cursor.fetchone()
        return Response({'message': 'data'})

@api_view(['DELETE', ])
def api_eliminar_articulo_view(request, sku):
    if request.method == 'DELETE':
        with connection.cursor() as cursor:
            articulo = cursor.execute("""SELECT delete_articulo(%s::smallint)""", [sku])
            articulo = cursor.fetchone()
        return Response({'message': 'data'})


