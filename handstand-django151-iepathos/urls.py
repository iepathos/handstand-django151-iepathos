from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL +'ico/favicon.ico')), #google chrome favicon fix
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='dashboard'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {}, 'logout',),
    url(r'^associate/$', TemplateView.as_view(template_name='associate.html'), name='associate'),
    url(r'^tinymce/', include('tinymce.urls')),
)
