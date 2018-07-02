#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from connection import Connection
from interface import Interface

class Data:
    def start_program(self):

        def list_musics():
            music_data = self.connection.get_music_list()
            band_data = self.connection.get_band_list()
            self.interface.list_music_view_header()
            for music in music_data:
                music_list = {
                    'music_name': music['name'],
                    'music_duration': music['duration'],
                    'music_release': music['release'],
                }
                for band in band_data:
                    if music['band'] == band['id']:
                        music_list['music_band'] = band['name']

                self.interface.list_music_view(music_list)

            self.interface.click_to_continue_view()
            menu_get()

        def list_bands():
            band_data = self.connection.get_band_list()
            genre_data = self.connection.get_genre_list()
            record_data = self.connection.get_record_list()
            self.interface.list_band_view_header()
            for band in band_data:
                band_list = {
                    'band_name': band['name'],
                }
                for genre in genre_data:
                    if band['genre'] == genre['id']:
                        band_list['band_genre'] = genre['name']
                for record in record_data:
                    if band['record'] == record['id']:
                        band_list['band_record'] = record['name']
                self.interface.list_band_view(band_list)

            self.interface.click_to_continue_view()
            menu_get()

        def list_genres():
            genre_data = self.connection.get_genre_list()
            self.interface.list_genre_view_header()
            for genre in genre_data:
                genre_list = {
                    'genre_name': genre['name']
                }
                self.interface.list_genre_view(genre_list)

            self.interface.click_to_continue_view()
            menu_get()

        def list_records():
            record_data = self.connection.get_record_list()
            self.interface.list_record_view_header()
            for record in record_data:
                record_list = {
                    'record_name': record['name']
                }
                self.interface.list_record_view(record_list)

            self.interface.click_to_continue_view()
            menu_get()

        def list_playlists():
            playlist_data = self.connection.get_playlist_list()
            music_data = self.connection.get_music_list()
            band_data = self.connection.get_band_list()
            self.interface.list_playlist_view_header()

            for playlist in playlist_data:
                playlist_list = {
                    'playlist_name': playlist['name']
                }
                self.interface.list_playlist_view(playlist_list)
                for music in music_data:
                    for each in playlist['music']:
                        if each is music['id']:
                            for band in band_data:
                                if music['band'] is band['id']:
                                    self.interface.list_playlist_music_view(music['name'], band['name'])

            self.interface.click_to_continue_view()
            menu_get()

        def post_music():
            music_info = self.interface.insert_music()

            if music_info != None:
                self.connection.post_music(music_info)
            else:
                self.interface.try_again_message()
                self.interface.click_to_continue_view()

        def menu_get():
            menu_result_option = self.interface.menu_get()
            if menu_result_option == 0:
                self.interface.finish_message()
                exit()
            if menu_result_option < 0:
                self.interface.incorrect_value_message()
                self.interface.try_again_message()
                menu_get()
            elif menu_result_option is 1:
                list_musics()
            elif menu_result_option is 2:
                list_bands()
            elif menu_result_option is 3:
                list_genres()
            elif menu_result_option is 4:
                list_records()
            elif menu_result_option is 5:
                list_playlists()
            elif menu_result_option is 6:
                menu_get()

        def menu_post():
            menu_result_option = self.interface.menu_post()

            if menu_result_option < 0:
                self.interface.incorrect_value_message()
                self.interface.try_again_message()
                menu_post()
            elif menu_result_option is 1:
                post_music()
            elif menu_result_option is 2:
                list_bands()
            elif menu_result_option is 3:
                list_genres()
            elif menu_result_option is 4:
                list_records()
            elif menu_result_option is 5:
                list_playlists()
            elif menu_result_option is 6:
                menu_get_post()

        def menu_get_post():
            menu_result_option = self.interface.menu_get_post()

            if menu_result_option is 0:
                self.interface.finish_message()
                exit()
            elif menu_result_option < 0:
                self.interface.incorrect_value_message()
                self.interface.try_again_message()
                menu_get_post()
            elif menu_result_option is 1:
                menu_get()
            else:
                menu_post()

        menu_get()

    def __init__(self):
        self.connection = Connection()
        self.interface = Interface()
