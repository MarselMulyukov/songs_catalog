from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class MusicPerformer(models.Model):
    name = models.CharField(
        verbose_name='Имя исполнителя',
        max_length=40,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Музыкальный исполнитель'
        verbose_name_plural = 'Музыкальные исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(
        verbose_name='Название альбома',
        max_length=40,
        unique=True
    )
    music_performer = models.ForeignKey(
        MusicPerformer,
        verbose_name='Музыкальный исполнитель',
        related_name='albums',
        on_delete=models.CASCADE
    )
    release_year = models.PositiveIntegerField(
        verbose_name='Год выхода',
        validators=(
            MinValueValidator(1950),
            MaxValueValidator(timezone.now().year)
        )
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(
        verbose_name='Название песни',
        max_length=40
    )
    albums = models.ManyToManyField(
        Album,
        verbose_name='Альбомы',
        through='AlbumSongs'
    )

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.title


class AlbumSongs(models.Model):
    album = models.ForeignKey(
        Album,
        verbose_name='Альбом',
        related_name='album_songs',
        on_delete=models.CASCADE
    )
    song = models.ForeignKey(
        Song,
        verbose_name='Название песни',
        related_name='album_songs',
        on_delete=models.CASCADE
    )
    serial_number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(30),
        )
    )

    class Meta:
        ordering = ('serial_number',)
        verbose_name = 'Песня альбома'
        verbose_name_plural = 'Песни альбома'
        constraints = (
            models.UniqueConstraint(
                fields=(
                    'album',
                    'song'
                ),
                name='unique_albums_song',
            ),
            models.UniqueConstraint(
                fields=(
                    'serial_number',
                    'song'
                ),
                name='unique_songs_serial_number',
            )
        )
