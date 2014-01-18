from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from hirepagesApp.views import signup, login, logout, create_looking_page
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hirepages.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^signup$', signup),
    url(r'^login$', login),
    url(r'^logout$', logout),
    url(r'^createlooking$', create_looking_page)

    #url(r'^admin/', include(admin.site.urls)),
) 

urlpatterns += staticfiles_urlpatterns()
