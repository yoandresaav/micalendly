# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ReservaEstudiante, DisponibilidadHoraria


@admin.register(ReservaEstudiante)
class ReservaEstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'comentario', 'created', 'updated')
    list_filter = ('estudiante', 'created', 'updated')


@admin.register(DisponibilidadHoraria)
class DisponibilidadHorariaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'profesor',
        'estudiantes_permitidos',
        'fecha',
        'hora_inicio',
        'tiempo_minutos',
        'comentario',
        'created',
        'updated',
    )
    list_filter = ('profesor', 'fecha', 'created', 'updated')