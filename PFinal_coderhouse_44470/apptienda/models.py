from django.db import models

# Create your models here.

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name= 'Nombre')
    marca = models.CharField(max_length=100, verbose_name= 'Marca')
    precio = models.IntegerField(verbose_name= 'Precio', null=True)
    imagen = models.ImageField(upload_to='Imagenes/',verbose_name='Imagen', null= True)
    descripcion= models.TextField(verbose_name= 'Descripción', null=True)
    
    def __str__(self):
        fila = 'Nombre:' + self.nombre + '-' + 'Descripcion:' + self.descripcion + 'Precio:' + self.categoria
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()