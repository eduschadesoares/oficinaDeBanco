from django.conf.urls import url
from . import views

from .views import status

app_name = 'music'

urlpatterns = [
    url(r'^status/', status, name='status'),

    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name='music-detail'),

    url(r'^bands/$', views.BandList.as_view(), name='band-list'),
    url(r'^band/(?P<pk>[0-9]+)/$', views.BandDetail.as_view(), name='band-detail'),

    url(r'^records/$', views.RecordList.as_view(), name='record-list'),
    url(r'^record/(?P<pk>[0-9]+)/$', views.RecordDetail.as_view(), name='record-detail'),

    url(r'^genres/$', views.GenreList.as_view(), name='genre-list'),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.GenreDetail.as_view(), name='genre-detail'),

    url(r'^playlists/$', views.PlaylistList.as_view(), name='playlist-list'),
    url(r'^playlist/(?P<pk>[0-9]+)/$', views.PlaylistDetail.as_view(), name='playlist-detail'),

]