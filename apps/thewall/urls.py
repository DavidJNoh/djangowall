from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^clear$', views.clear),
    url(r'^message$', views.message),
    url(r'^comment/(?P<id>\d+)$', views.comment),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^messagedelete/(?P<id>\d+)$', views.messagedelete)

]    