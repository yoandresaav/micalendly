from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    dashboard_init, ProfesorIndex, EstudianteIndex,
    ProfesorDisponibleView, ProfesorHorariosView, profesor_eliminar_horario,
    estudiante_reservar, EstudianteHorarioView, estudiante_eliminar_horario
)

app_name = 'dashboard'

urlpatterns = [
    url(r'^inicio/$', dashboard_init, name='inicio'),

    url(r'^profesor/$', ProfesorIndex.as_view(), name='profesor'),
    url(r'^profesor/disponible/$', ProfesorDisponibleView.as_view(), name='profesor-disponible'),
    url(r'^profesor/horarios/$', ProfesorHorariosView.as_view(), name='profesor-horarios'),
    url(r'^profesor/horarios/(?P<pk>\d+)/eliminar/$', profesor_eliminar_horario, name='profesor-eliminar-horarios'),
    
    url(r'^estudiante/$', EstudianteIndex.as_view(), name='estudiante'),
    url(r'^estudiante/horarios/$', EstudianteHorarioView.as_view(), name='estudiante-horarios'),
    url(r'^estudiante/horarios/(?P<pk>\d+)/reservar/$', estudiante_reservar, name='estudiante-reservar'),
    url(r'^estudiante/horarios/(?P<pk>\d+)/eliminar/$', estudiante_eliminar_horario, name='estudiante-eliminar-horarios'),
]
