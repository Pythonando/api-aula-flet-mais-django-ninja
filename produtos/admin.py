from django.contrib import admin
from .models import Produto, Categoria

admin.site.register(Categoria)
admin.site.register(Produto)
