from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

@api_view(['GET'], )
def api_list_departamento_view(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = cursor.execute("SELECT get_departamentos()")
            query = cursor.fetchone()
            if not query[0]:
                return Response({'mesagge': 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        return Response({'message': 'success','data':query[0]})