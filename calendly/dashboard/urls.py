from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    dashboard_init, ProfesorIndex, EstudianteIndex,
    ProfesorDisponibleView,
)

app_name = 'dashboard'

urlpatterns = [
    url(r'^inicio/$', dashboard_init, name='inicio'),

    url(r'^profesor/$', ProfesorIndex.as_view(), name='profesor'),
    url(r'^profesor/disponible/$', ProfesorDisponibleView.as_view(), name='profesor-disponible'),
    
    url(r'^estudiante/$', EstudianteIndex.as_view(), name='estudiante'),
]
