from django.conf.urls import patterns, url

from hola import views

urlpatterns = patterns('',
	#ex: /hola/
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^sign$', views.sign, name='sign'),
)
