from django.db import models

# Create your models here.
class m_categoria(models.Model):
    nombre = models.CharField(max_length=100)
    ruta = models.CharField(max_length=100, null=True, blank = True, default = '#')

    def __str__(self):
        return self.nombre

class m_subcategoria(models.Model):
    nombre = models.CharField(max_length=100)
    ruta = models.CharField(max_length=100)
    categoria = models.ForeignKey(m_categoria,on_delete=models.SET_NULL,null=True,related_name='Subcategorias')

    def __str__(self):
        return self.nombre