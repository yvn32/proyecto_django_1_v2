from django.db import models

# Create your models here.
class producto(models.Model):
  #codigo = models.IntegerField()
  nombre = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=30)
  disponible = models.BooleanField()
  fechaIncorporacion = models.DateField()
  idProveedor = models.IntegerField()

