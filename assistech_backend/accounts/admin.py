from django.contrib import admin
from .models import Cliente, Soporte, JefeSoporte

admin.site.register(Cliente)
admin.site.register(Soporte)
admin.site.register(JefeSoporte)