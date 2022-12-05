from django.db import models
from apps.departamento.models import Departamento
from apps.clase.models import Clase
from apps.familia.models import Familia

# Create your models here.
class Articulo(models.Model):
    DESCONTINUADO = (
        (1, 'Activado'),
        (0, 'Desactivado')
    )
    # Eliminado logico
    ESTATUS = (
        (1, 'Activo'),
        (0, 'Inactivo')
    )
    sku = models.SmallIntegerField()
    nombre = models.CharField(max_length = 15)
    marca = models.CharField(max_length = 15)
    modelo = models.CharField(max_length = 20)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete = models.CASCADE)
    familia =models.ForeignKey(Familia, on_delete = models.CASCADE)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(default='1900-01-01')
    stock = models.SmallIntegerField()
    cantidad = models.SmallIntegerField()
    descontinuado = models.SmallIntegerField(default = 0, choices = DESCONTINUADO)
    estatus = models.SmallIntegerField(default = 1, choices = ESTATUS)
    
    class Meta:
      db_table = 'articulo'
    
    def __str__(self):
        return f'{self.sku}-{self.nombre}'