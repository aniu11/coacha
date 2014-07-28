from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coacha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^wow/', include('wow.urls')),
    url(r'^infoma/', include('infoma.urls')),
    url(r'^', include('navigate.urls')),
    url(r'^static/', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()

