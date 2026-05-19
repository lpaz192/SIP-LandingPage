from django.contrib import admin
from .models import InfoTicket, TicketHistorial, TicketComentario, TicketAsignacion

admin.site.register(InfoTicket)
admin.site.register(TicketHistorial)
admin.site.register(TicketComentario)
admin.site.register(TicketAsignacion)