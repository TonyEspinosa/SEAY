from django.contrib import admin
from django.urls import path, include

#Agregados para archivos estáticos
from django.conf import settings
from django.conf.urls.static import static

#Importar las vistas del proyecto
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.v_home, name = "u_home"),

# Agregar AdminLTE
    path('', include('admin_adminlte.urls')),

# Páginas Staticas de Prueba
    path('presentacion', views.v_presentacion, name = "u_presentacion"),

    path('secretaria', views.v_secretaria, name = "u_secretaria"),

    path('comite', views.v_comite, name = "u_comite"),

    path('cpc', views.v_cpc, name = "u_cpc"),

    path('directorio', views.v_directorio, name = "u_directorio"),

    path('blog', views.v_blog, name = "u_blog"),

    path('noticias', views.v_noticias, name = "u_noticias"),

    path('transparencia', views.v_transparencia, name = "u_transparencia"),

    path('unidad', views.v_unidad, name = "u_unidad"),

    path('ifp', views.v_ifp, name = "u_ifp"),

    path('archivo', views.v_archivo, name = "u_archivo"),

    path('marco', views.v_marco, name = "u_marco"),

    path('privacidad', views.v_privacidad, name = "u_privacidad"),

    path('peay', views.v_peay, name = "u_peay"),

    path('recomendaciones', views.v_recomendaciones, name = "u_recomendaciones"),

    path('reconocimientos', views.v_reconocimientos, name = "u_reconocimientos"),

    path('convenios', views.v_convenios, name = "u_convenios"),

    path('cee', views.v_cee, name = "u_cee"),

    path('mq', views.v_mq, name = "u_mq"),

    path('integridad', views.v_integridad, name = "u_integridad"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
