from django.shortcuts import render, redirect
from plantasapp.models import Pedido, Comprador
import io
from reportlab.pdfgen import canvas
from django.http import FileResponse


def index(request):
    return render(request, 'index.html')


def cargar_datos(request):
    if request.method == 'POST':
        comprador = request.POST['comprador']
        if int(comprador) < 0:
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            direccion = request.POST['dir']
            cel = request.POST['cel']
            detalle = request.POST['detalle']
            c = Comprador(nombre=nombre, apellido=apellido, direccion=direccion, celular=cel, detalle=detalle)
            comp = Comprador.objects.filter(nombre=nombre, apellido=apellido)
            if not comp:
                c.save()
                compr = Comprador.objects.get(nombre=nombre, apellido=apellido)
                idd = compr.id
                return render(request, 'carga_datos_pedido.html', {'comprador': idd, 'precioTotal': "0.00"})
            else:
                return render(request, 'carga_datos_pedido.html', {'comprador': comp[0].id, 'precioTotal': "0.00"})
        else:
            comp = Comprador.objects.get(pk=int(comprador))
            pedido = request.POST['pedido']
            cant = request.POST['cantidad']
            pu = request.POST['precioUnitario']
            pt = float(request.POST['precioTotal'])
            p = Pedido(comprador=comp, pedido=pedido, cant=cant, pu=pu)
            p.save()
            pr = float(pu) * int(cant)
            tot = pt + pr
            #if tott:
             #   pass
            return render(request, 'carga_datos_pedido.html', {'comprador': int(comprador),
                                                               'precioTotal': str(tot)})
    else:
        return render(request, 'carga_datos_comprador.html', {'comprador': -1})


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def listar_pedidos_necesarios(request):
    pedidos = Pedido.objects.all()
    compradores = Comprador.objects.all()
    if request.method == 'POST':
        lista_de_pedido = []
        for ped in pedidos:
            pk = ped.pk
            ped_id = request.POST[str(pk)]
            if ped_id == 'yes':
                lista_de_pedido.append(ped)
        return render(request, 'impresion1.html', {'pedidos':lista_de_pedido})
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos, 'compradores': compradores})


def listar_pedidos_repartir(request):
    pedidos = Pedido.objects.all()
    compradores = Comprador.objects.all()
    if request.method == 'POST':
        lista_de_pedido = []
        lista_de_compradores = []
        for comp in compradores:
            pk = comp.pk
            comp_id = request.POST[str(pk)]
            if comp_id == 'yes':
                lista_de_compradores.append(comp)
                for ped in pedidos:
                    if ped.comprador.pk == comp.pk:
                        ped.a_entregar = True
                        ped.save()
                        lista_de_pedido.append(ped)
        return render(request, 'impresion2.html', {'compradores': lista_de_compradores, 'pedidos': lista_de_pedido})
    return render(request, 'listar_pedidos_repartir.html', {'pedidos': pedidos, 'compradores': compradores})


def listar_pedidos_cargar(request):
    pedidos = Pedido.objects.filter(a_entregar=True)
    if request.method == 'POST':
        lista_de_pedido = []
        for ped in pedidos:
            pk = ped.pk
            ped_id = request.POST[str(pk)]
            if ped_id == 'yes':
                lista_de_pedido.append(ped)
        return render(request, 'impresion3.html', {'pedidos': lista_de_pedido})
    return render(request, 'listar_pedidos_cargar.html', {'pedidos': pedidos})
