from nptime import nptime

from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_time
from datetime import timedelta, date, datetime

User = get_user_model()


class DisponibilidadManager(models.Manager):
    def is_posible_create(self, user, form):
        fecha_str = form.data.get('fecha')
        hora_str = form.data.get('hora_inicio')

        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        tiempo = int(form.data.get('tiempo_minutos'))
        hora_str, min_str = hora_str.split(':')
        hora_inicial = nptime(int(hora_str), int(min_str))
        hora_final = hora_inicial + timedelta(minutes=tiempo)

        qs = self.get_queryset().filter(
            fecha=fecha, profesor=user,
            hora_inicio__range=[hora_inicial, hora_final]
        )

        if qs:
            error = "Ya tienes el día %s y hora %s reservado." % (fecha_str, hora_str)
            error_code = "invalid_date"
            raise forms.ValidationError(error, code=error_code)


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

    objects = DisponibilidadManager()

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