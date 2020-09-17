from django.db import models


class Comprador(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    celular = models.IntegerField(null=True)
    direccion = models.CharField(max_length=25)
    detalle = models.TextField(null=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    class Meta:
        verbose_name_plural = 'Compradores'


class Pedido(models.Model):
    comprador = models.ForeignKey('Comprador', on_delete=models.SET_NULL, null=True)
    pedido = models.CharField(max_length=25)
    cant = models.IntegerField(null=True)
    pu = models.FloatField(null=True)
    a_entregar = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.pedido

    class Meta:
        verbose_name_plural = 'Pedidos'
# Create your models here.
