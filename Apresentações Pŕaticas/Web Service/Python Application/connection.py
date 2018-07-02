#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json

localhost = '127.0.0.1'
port = '9000'

class Connection:
    def __init__(self):
        self.connection = self.estabilish_connection(localhost, port)

    def estabilish_connection(self, localhost, port):
        url = 'http://{}:{}/status'.format(localhost, port)
        try:
            connection = requests.get(url)
            if connection:
                print("╔┅▶  Status: {}\n╠┅▶ ✓ Connected to server!".format(connection.reason))
            return True
        except Exception as error:
            print("Could not connect to server!")
            print(error)
            exit()

# GET METHODS

    def get_music_list(self):
        search = 'musics'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        try:
            music_data = requests.get(url).json()
        except Exception as error:
            print(error)
        return music_data

    def get_band_list(self):
        search = 'bands'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        try:
            band_data = requests.get(url).json()
        except Exception as error:
            print(error)
        return band_data

    def get_genre_list(self):
        search = 'genres'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        try:
            genre_data = requests.get(url).json()
        except Exception as error:
            print(error)
        return genre_data

    def get_record_list(self):
        search = 'records'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        try:
            record_data = requests.get(url).json()
        except Exception as error:
            print(error)
        return record_data

    def get_playlist_list(self):
        search = 'playlists'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        try:
            playlist_data = requests.get(url).json()
        except Exception as error:
            print(error)
        return playlist_data

# POST METHODS

    def post_music(self, music_info):
        search = 'musics/'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        try:
            playlist_data = requests.post(url, music_info)
            print(playlist_data.reason)

        except Exception as error:
            print(error)
