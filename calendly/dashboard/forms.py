from django import forms
from django.forms import ModelForm

from .models import DisponibilidadHoraria

class DisponibilidadHorariaForm(ModelForm):
    class Meta:
        model = DisponibilidadHoraria
        fields = [
            'titulo', 'estudiantes_permitidos', 'fecha', 'hora_inicio',
            'tiempo_minutos', 'comentario'
        ]
        widgets = {
            'fecha': forms.DateInput(
                attrs={'class': 'datepicker', 'autocomplete': 'off'}
            ),
            'hora_inicio': forms.TimeInput(
                attrs={'class': 'timepicker', 'autocomplete': 'off'}
            )
        }