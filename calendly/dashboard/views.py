from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import DisponibilidadHorariaForm
from .models import DisponibilidadHoraria, ReservaEstudiante

@login_required
def dashboard_init(request):
    user = request.user
    if user.is_profesor:
        return redirect(reverse_lazy('dashboard:profesor'), permanent=True)
    else:
        return redirect(reverse_lazy('dashboard:estudiante'), permanent=True)


class ProfesorIndex(LoginRequiredMixin, ListView):
    template_name = 'dashboard/profesor/inicio.html'
    def get_queryset(self):
        return ReservaEstudiante.objects.filter(
            disponibilidad__profesor=self.request.user
        )

class ProfesorDisponibleView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/profesor/disponible.html'
    form_class = DisponibilidadHorariaForm
    success_url = '/dashboard/profesor/'
    def form_valid(self, form):
        form.instance.profesor = self.request.user
        form.save()
        messages.success(self.request, 'Guardado tu horario con éxito.')
        return super().form_valid(form)

class ProfesorHorariosView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/profesor/horarios.html'

    def get_queryset(self):
        return DisponibilidadHoraria.objects.filter(
            profesor=self.request.user
        ).order_by('-fecha')

@login_required
def profesor_eliminar_horario(request, pk):
    disponibilidad = DisponibilidadHoraria.objects.filter(pk=pk, profesor=request.user)
    if not disponibilidad:
        messages.warning(request, 'Esa disponibilidad de horario no existe')
    else:
        disponibilidad.delete()
        messages.success(request, 'Eliminada la disponibilidad')
    return redirect(reverse_lazy('dashboard:profesor'))

class EstudianteIndex(LoginRequiredMixin, ListView):
    template_name = 'dashboard/estudiante/inicio.html'

    def get_queryset(self):
        return DisponibilidadHoraria.objects.all()

@login_required
def estudiante_reservar(request, pk):
    disponibilidad = DisponibilidadHoraria.objects.filter(pk=pk).first()
    if disponibilidad:
        ReservaEstudiante.objects.create(
            estudiante=request.user,
            disponibilidad=disponibilidad,
            comentario='Reserva automatizada'
        )
        messages.success(request, 'Se ha reservado el horario')
    else:
        messages.warning(request, 'Lo sentimos no se ha reservado')
    return redirect(reverse_lazy('dashboard:estudiante'))

class EstudianteHorarioView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/estudiante/horarios.html'
    def get_queryset(self):
        return ReservaEstudiante.objects.filter(
            estudiante=self.request.user
        ).order_by('-created')

@login_required
def estudiante_eliminar_horario(request, pk):
    reserva = ReservaEstudiante.objects.filter(
        pk=pk, estudiante=request.user
    )
    if not reserva:
        messages.warning(request, 'Esta reserva de horario no existe')
    else:
        reserva.delete()
        messages.success(request, 'Eliminada la reserva de horario')
    return redirect(reverse_lazy('dashboard:estudiante'))
