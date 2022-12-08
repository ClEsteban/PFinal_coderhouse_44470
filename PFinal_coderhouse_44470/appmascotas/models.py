from django.db import models


# Create your models here.

class mascotas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name= 'Nombre')
    tipo = models.CharField(max_length=100, verbose_name= 'Tipo')
    imagen = models.ImageField(upload_to='Imagenes/',verbose_name='Imagen', null= True)
    descripcion = models.TextField(verbose_name= 'Descripción', null=True)
    raza = models.CharField(verbose_name= 'Raza', max_length=100, null=True)

    def __str__(self):
        fila = f"Nombre: {self.nombre} - Tipo: {self.tipo} - Descripcion: {self.descripcion} - Raza: {self.raza}"
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
