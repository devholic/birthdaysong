from django.conf.urls import patterns, include, url
from django.contrib import admin
from timeline_web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'birthdaysong.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home),
    url(r'^share$', views.share),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^permission$', views.permission),
    url(r'^privacy$', views.privacy),
)
