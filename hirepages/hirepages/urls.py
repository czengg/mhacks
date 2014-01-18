from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from hirepagesApp.views import signup, login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hirepages.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup/$', signup),
    url(r'^login/$', login),
    url(r'^createrecruit/$', createrecruit),
    url(r'^createlook/$', createlook),
    #url(r'^admin/', include(admin.site.urls)),
)
