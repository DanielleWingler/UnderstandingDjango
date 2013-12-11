# There should be a .pyc file by the same name at creation.

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
     
urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', 'blog.views.index'),
  url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)
