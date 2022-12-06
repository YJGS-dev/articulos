from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length = 50)
    
    class Meta:
      db_table = 'departamento'
    
    def __str__(self):
        return self.nombre