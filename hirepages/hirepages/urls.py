from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hirepages.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login),
    url(r'^createrecruit/$', views.createrecruit),
    url(r'^createlook/$', views.createlook),

    url(r'^admin/', include(admin.site.urls)),
)
