from django.contrib import admin

# Register your models here.
from .models import m_categoria, m_subcategoria

admin.site.register(m_categoria)
admin.site.register(m_subcategoria)
