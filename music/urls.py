from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/album.id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album.id/fav
   # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
