from django.conf.urls import patterns, url
from wow import views

urlpatterns=patterns('',
	url(r'^$', views.result, name='index'),
	url(r'^auth$', views.auth, name='auth'),
	url(r'^result$', views.result, name='result'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^update$', views.update, name='update'),
	url(r'^edit$', views.edit, name='edit'),
	url(r'^comment$', views.comment, name='comment'),
	)