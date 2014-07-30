from django.conf.urls import patterns, url
from blog import views

urlpatterns=patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^passage$', views.passage, name='passage'),
	url(r'^content$', views.content, name='content'),
	)