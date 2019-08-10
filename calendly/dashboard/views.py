from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView



def dashboard_init(request):
    user = request.user
    if user.is_profesor:
        return redirect(reverse_lazy('dashboard:profesor'), permanent=True)
    else:
        return redirect(reverse_lazy('dashboard:estudiante'), permanent=True)


class ProfesorIndex(TemplateView):
    template_name = 'dashboard/profesor/inicio.html'

class ProfesorDisponibleView(TemplateView):
    template_name = 'dashboard/profesor/disponible.html'

class EstudianteIndex(TemplateView):
    template_name = 'dashboard/estudiante/inicio.html'