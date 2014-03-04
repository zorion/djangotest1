from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")), #from tuto03
    url(r'^hola/', include('hola.urls', namespace="hola")), #from django-nonrel
    url(r'^admin/', include(admin.site.urls)),
)
# https://developers.google.com/appengine/articles/django-nonrel
