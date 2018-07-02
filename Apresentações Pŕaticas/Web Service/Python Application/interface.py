#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Interface:

    def list_music_view_header(self):
        print("║")
        print("║   Músicas")
        print("║   {0:40}".format('Nome'), end=' ')
        print(" {0:40}".format('Banda'), end=' ')
        print(" {0:20}".format('Duração'), end=' ')
        print(" {}".format('Lançamento'))

    def list_band_view_header(self):
        print("║")
        print("║   Bandas")
        print("║   {0:40}".format('Nome'), end=' ')
        print(" {0:40}".format('Gênero'), end=' ')
        print("{}".format('Gravadora'))

    def list_genre_view_header(self):
        print("║")
        print("║   Gêneros")
        print("║   {0:40}".format('Nome'))


    def list_record_view_header(self):
        print("║")
        print("║   Gravadoras")
        print("║   {0:40}".format('Nome'))

    def list_playlist_view_header(self):
        print("║")
        print("║   Playlists")

    def list_music_view(self, music_list):
        print('║ ━ {0:40} '.format(music_list['music_name']), end=' ')
        print('{0:40} '.format(music_list['music_band']), end=' ')
        print('{0:20} '.format(music_list['music_duration']), end=' ')
        print('{0:20}'.format(music_list['music_release']), end=' ')
        print('')

    def list_band_view(self, band_list):
        print('║ ━ {0:40} '.format(band_list['band_name']), end=' ')
        print('{0:40}'.format(band_list['band_genre']), end=' ')
        print('{}'.format(band_list['band_record']), end=' ')
        print('')

    def list_genre_view(self, genre_list):
        print('║ ━ {0:40}'.format(genre_list['genre_name']))

    def list_record_view(self, record_list):
        print('║ ━ {0:40}'.format(record_list['record_name']))

    def list_playlist_view(self, playlist_list):
        print("║")
        print('║  {0:40}'.format(playlist_list['playlist_name']))

    def list_playlist_music_view(self, music, band):
        print('║  ━ {0:40}'.format(music), band)

    def click_to_continue_view(self):
        print("║")
        print('╠┅▶ ⌨  Pressione enter para continuar', end='')
        none = input()

    def finish_message(self):
        print("║")
        print("╚┅▶ O programa será encerrado! ㋡")

    def incorrect_value_message(self):
        print("╠┅▶  Valor incorreto")

    def invalid_value_message(self):
        print("╠┅▶  Valor inválido")

    def try_again_message(self):
        print("╠┅▶  Tente novamente!")

    def insert_music(self):
        print("╠┅▶  Inserir música")
        print("║")
        try:
            print("╠┅▶ ⌨  Nome da música: ", end="")
            music_name = str(input())
            print("╠┅▶ ⌨  Banda: ", end="")
            music_band = int(input())
            print("╠┅▶ ⌨  Duração: ", end="")
            music_duration = str(input())
            print("╠┅▶ ⌨  Lançamento: ", end="")
            music_release = str(input())
        except ValueError:
            print("║")
            print("╠┅▶ ❎ Valor irregular")
            return

        music_info = {
            'name': music_name,
            'duration': music_duration,
            'release': music_release,
            'band': music_band,
        }

        return music_info

    def menu_get_post(self):
        print("╠════════════════════════╗")
        print("║          MENU          ║")
        print("╠═════╤══════════════════╣")
        print("║  1  │       GET        ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║     │                  ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  0  │       EXIT       ║")
        print("╠═════╧══════════════════╝")
        print("╠┅▶ ⌨  Escolha uma opção:", end="")
        try:
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 0:
                return 0
            else:
                return -1
        except ValueError:
            return -1

    def menu_get(self):
        print("╠════════════════════════╗")
        print("║        MENU GET        ║")
        print("╠═════╤══════════════════╣")
        print("║  1  │      Músicas     ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  2  │      Bandas      ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  3  │      Gêneros     ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  4  │    Gravadoras    ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  5  │     Playlists    ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  0  │       Sair       ║")
        print("╠═════╧══════════════════╝")
        print("╠┅▶ ⌨  Escolha uma opção:", end="")
        try:
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return 3
            elif choice == 4:
                return 4
            elif choice == 5:
                return 5
            elif choice == 0:
                return 0
            else:
                return -1
        except ValueError:
            return -1

    def menu_post(self):
        print("╠════════════════════════╗")
        print("║        MENU POST       ║")
        print("╠═════╤══════════════════╣")
        print("║  1  │ Inserir Músicas  ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  2  │ Inserir Bandas   ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  3  │ Inserir Gêneros  ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  4  │Inserir Gravadora ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  5  │Inserir Playlists ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  6  │      Voltar      ║")
        print("╠═════╧══════════════════╝")
        print("╠┅▶ ⌨  Escolha uma opção:", end="")
        try:
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return 3
            elif choice == 4:
                return 4
            elif choice == 5:
                return 5
            elif choice == 6:
                return 6
            elif choice == 0:
                return 0
            else:
                return -1
        except ValueError:
            return -1
