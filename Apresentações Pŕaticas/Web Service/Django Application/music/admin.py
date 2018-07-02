from django.contrib import admin

from .models import (Music,
                     Band,
                     Genre,
                     Record,
                     Playlist,
                     )

class MusicAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'band',
                    'duration',
                    'release',
                    )

    class Meta:
        model = Music

class BandAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'genre',
                    'record',
                    )

    class Meta:
        model = Band

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )

    class Meta:
        model = Genre


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )

    class Meta:
        model = Record


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )

    class Meta:
        model = Playlist


admin.site.register(Music, MusicAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Playlist, PlaylistAdmin)
