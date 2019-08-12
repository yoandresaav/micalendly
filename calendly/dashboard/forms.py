import datetime
from django import forms
from django.forms import ModelForm

from .models import DisponibilidadHoraria

class DisponibilidadHorariaForm(ModelForm):
    tiempo_minutos = forms.IntegerField(
        min_value=30,
        max_value=240,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tiempo_minutos'].initial = 30
    
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

    def clean_tiempo_minutos(self):
        tiempo_minutos = self.cleaned_data.get('tiempo_minutos')
        return datetime.timedelta(minutes=int(tiempo_minutos))