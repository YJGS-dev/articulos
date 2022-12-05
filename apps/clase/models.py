from django.db import models
from apps.departamento.models import Departamento

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length = 50)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    
    class Meta:
      db_table = 'clase'

    def __str__(self):
        return self.nombre