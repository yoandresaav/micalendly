from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DisponibilidadHoraria(models.Model):
    titulo = models.CharField(max_length=120)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE)
    estudiantes_permitidos = models.PositiveIntegerField(default=1)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    tiempo_minutos = models.PositiveIntegerField(default=30)
    comentario = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Disponibilidad de %s' % self.profesor

class ReservaEstudiante(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    disponibilidad = models.ForeignKey(DisponibilidadHoraria, on_delete=models.CASCADE, null=True)
    comentario = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
            return 'Reserva %s' % self.estudiante