from django.shortcuts import render

#Para efectos de pruebas
from django.http import HttpResponse

#Importa el Navbar
from apps.DinNavBar.models import m_categoria
from django.db.models import Count


# Paginas Publicas
def v_home(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'inicio.html', context)

#Para efectos de pruebas
#def v_home(request):
#    return HttpResponse("Hola")

def v_presentacion(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/01presentacion.html', context)

def v_secretaria(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/02secretaria.html', context)

def v_comite(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/03comite.html', context)

def v_cpc(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/04cpc.html', context)

def v_directorio(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/05directorio.html', context)

def v_blog(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/06blog.html', context)

def v_noticias(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/07noticias.html', context)

def v_transparencia(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/08transparencia.html', context)

def v_unidad(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/09unidad.html', context)

def v_ifp(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/10ifp.html', context)

def v_archivo(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/11archivo.html', context)

def v_marco(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/12marco.html', context)

def v_privacidad(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/13privacidad.html', context)

def v_peay(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/14peay.html', context)

def v_recomendaciones(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/15recomendaciones.html', context)

def v_reconocimientos(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/16reconocimientos.html', context)

def v_convenios(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/17convenios.html', context)

def v_cee(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/18cee.html', context)

def v_mq(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/19mq.html', context)

def v_integridad(request):
    catego = m_categoria.objects.annotate(
        subCat = Count('Subcategorias'))
    context =  {'catego':catego}
    return render(request, 'tempo/20integridad.html', context)