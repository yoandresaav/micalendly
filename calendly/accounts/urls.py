
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import (
    SignUpView, LoginAccountView
)

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', LoginAccountView.as_view(), name='login'),
]
