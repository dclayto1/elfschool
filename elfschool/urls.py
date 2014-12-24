from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elfschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls')),
    url(r'^programs/', include('programs.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^contact/', include('contact.urls')),
    url('', include('home.urls')),
)
