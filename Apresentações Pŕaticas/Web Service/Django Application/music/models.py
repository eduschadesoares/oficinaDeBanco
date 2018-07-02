from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False,
                            unique=True,
                            verbose_name='Gravadora',
                            )

    class Meta:
        verbose_name = 'Gravadora'
        verbose_name_plural = 'Gravadora'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False,
                            unique=True,
                            verbose_name='Gênero'
                            )
    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            blank=False,
                            null=False,
                            verbose_name='Nome da Banda',
                            )
    genre = models.ForeignKey(Genre,
                              verbose_name='Gênero',
                              on_delete=models.CASCADE,
                              )

    record = models.ForeignKey(Record,
                               verbose_name='Gravadora',
                               on_delete=models.CASCADE,
                               )

    class Meta:
        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=100,
                            unique=False,
                            blank=False,
                            null=False,
                            verbose_name='Nome da música')
    band = models.ForeignKey(Band,
                             verbose_name='Banda',
                             on_delete=models.CASCADE,
                             )
    duration = models.DurationField(blank=False,
                                    null=False,
                                    verbose_name='Duração da música',
                                    )
    release = models.DateField(auto_now_add=False,
                               blank=True,
                               verbose_name='Data de Lançamento',
                               )

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False,
                            unique=False,
                            verbose_name='Playlist'
                            )
    music = models.ManyToManyField(Music,
                                   verbose_name='Música',
                                   )