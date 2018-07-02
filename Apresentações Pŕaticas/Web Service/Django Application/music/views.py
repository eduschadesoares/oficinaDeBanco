from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

import json

from rest_framework import generics
from .serializers import (MusicSerializer,
                          BandSerializer,
                          RecordSerializer,
                          GenreSerializer,
                          PlaylistSerializer,
                          )
from .models import (Music,
                     Band,
                     Record,
                     Genre,
                     Playlist,
                     )

# Create your views here.
class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    # authentication_classes = [OAuth2Authentication, SessionAuthentication]
    # permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )

def status(request):
    status = {'status': 'OK'}

    data = json.dumps(status)

    return HttpResponse(data)
