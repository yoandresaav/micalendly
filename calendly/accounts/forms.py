
from django import forms
from django.conf import settings
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm
)

from django.contrib import messages
from django.contrib.auth import get_user_model


User = get_user_model()

class UserCreationWithEmailForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
        help_text='Requerido. Introduzca un correo válido'
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "is_profesor", "is_estudiante")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserCreationWithEmailForm, self).__init__(*args, **kwargs)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo {email} ya existe'.format(email=email)) 
        return email

    def clean(self):
        is_estudiante = self.cleaned_data["is_estudiante"]
        is_profesor = self.cleaned_data["is_profesor"]
        if not is_estudiante and not is_profesor:
            raise forms.ValidationError('Debe escoger Estudiante o Profesor')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_estudiante = bool(self.cleaned_data["is_estudiante"])
        user.is_profesor = bool(self.cleaned_data["is_profesor"])
        user.is_active = True
        if commit:
            try:
                user.save()
            except:
                return None
            return user
        return None


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    