from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^account/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^signup/$', TemplateView.as_view(template_name='signup.html')),
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('django.contrib.auth.urls')),

    # web site
    url(r'^features/$', TemplateView.as_view(template_name='web/features.html'), name='features'),
    url(r'^princing/$', TemplateView.as_view(template_name='web/princing.html'), name='princing'),
    url(r'^about/$', TemplateView.as_view(template_name='web/about.html'), name='about'),
    url(r'^$', TemplateView.as_view(template_name='web/index.html'), name='index'),
]
