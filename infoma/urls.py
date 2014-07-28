from django.conf.urls import patterns, url
from infoma import views

urlpatterns=patterns('',
	url(r'^$', views.result, name='result'),
	url(r'^self$', views.self, name='self'),
	url(r'^store_information$', views.store_information, name='store_information'),
	url(r'^result$', views.result, name='result'),
	url(r'^check$', views.check, name='check'),
	)