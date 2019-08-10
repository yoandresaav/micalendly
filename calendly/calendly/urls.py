from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^account/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^signup/$', TemplateView.as_view(template_name='signup.html')),
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
]
