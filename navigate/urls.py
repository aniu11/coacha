from django.conf.urls import patterns, url
from navigate import views

urlpatterns=patterns('',
	url(r'^$', views.navigate, name='navigate'),
	url(r'^aboutme', views.aboutme, name='aboutme'),
	)