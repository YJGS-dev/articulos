from django.db import models
from apps.clase.models import Clase

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length = 50)
    clase = models.ForeignKey(Clase, on_delete = models.CASCADE)

    class Meta:
      db_table = 'familia'

    def __str__(self):
        return self.nombre