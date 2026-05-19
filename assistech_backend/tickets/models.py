from django.db import models
from django.contrib.auth.models import User

class InfoTicket(models.Model):
    ESTADO_CHOICES = [
        ('ABIERTO',     'Abierto'),
        ('EN_PROCESO',  'En proceso'),
        ('RESUELTO',    'Resuelto'),
        ('CERRADO',     'Cerrado'),
    ]
    PRIORIDAD_CHOICES = [
        ('BAJA',    'Baja'),
        ('MEDIA',   'Media'),
        ('ALTA',    'Alta'),
        ('CRITICA', 'Crítica'),
    ]
    IMPACTO_CHOICES = [
        ('BAJO',  'Bajo'),
        ('MEDIO', 'Medio'),
        ('ALTO',  'Alto'),
    ]

    titulo              = models.CharField(max_length=200)
    descripcion         = models.TextField()
    categoria           = models.CharField(max_length=100, blank=True, null=True)
    estado              = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ABIERTO')
    prioridad           = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    fecha_creacion      = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_resolucion    = models.DateTimeField(blank=True, null=True)
    fecha_cierre        = models.DateTimeField(blank=True, null=True)
    solicitante         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    empresa             = models.CharField(max_length=100, blank=True, null=True)
    solucion_resumen    = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'info_tickets'


class TicketHistorial(models.Model):
    ticket          = models.ForeignKey(InfoTicket, on_delete=models.CASCADE, related_name='historial')
    estado_anterior = models.CharField(max_length=20, blank=True, null=True)
    estado_nuevo    = models.CharField(max_length=20, blank=True, null=True)
    fecha_cambio    = models.DateTimeField(auto_now_add=True)
    realizado_por   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historial_acciones')
    observacion     = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ticket_historial'


class TicketComentario(models.Model):
    ticket            = models.ForeignKey(InfoTicket, on_delete=models.CASCADE, related_name='comentarios')
    usuario           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    comentario        = models.TextField()
    fecha_comentario  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ticket_comentarios'


class TicketAsignacion(models.Model):
    ticket           = models.ForeignKey(InfoTicket, on_delete=models.CASCADE, related_name='asignaciones')
    soporte          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_asignados')
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    asignado_por     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asignaciones_realizadas', blank=True, null=True)
    activo           = models.BooleanField(default=True)

    class Meta:
        db_table = 'ticket_asignaciones'