from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UserCreationWithEmailForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationWithEmailForm

    def post(self, request, *args, **kwargs):
        form = UserCreationWithEmailForm(request.POST, request=request)
        if form.is_valid():
            user = form.save()

            # create new user
            if user is not None:
                messages.success(request, 'Ahora puedes entrar con tu usuario y contraseña')
                return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse('dasboard:inicio')
class LoginView(LoginView):
    template_name = 'accounts/login.html'