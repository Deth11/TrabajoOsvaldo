from django.contrib import admin
from plantasapp.models import Pedido, Comprador

# Register your models here.


class CompradorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre',)
    search_fields = ('apellido',)


admin.site.register(Comprador, CompradorAdmin)


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'comprador')
    search_fields = ('comprador',)


admin.site.register(Pedido, PedidoAdmin)

admin.site.site_header = 'Sitio de administracion de Plantas'
admin.site.index_title = 'Sitio de administracion de Plantas'
