# Generated by Django 4.1.7 on 2023-03-02 09:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название альбома')),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2023)], verbose_name='Год выхода')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='AlbumSongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Порядковый номер')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_songs', to='api.album', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Песня альбома',
                'verbose_name_plural': 'Песни альбома',
                'ordering': ('serial_number',),
            },
        ),
        migrations.CreateModel(
            name='MusicPerformer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Имя исполнителя')),
            ],
            options={
                'verbose_name': 'Музыкальный исполнитель',
                'verbose_name_plural': 'Музыкальные исполнители',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название песни')),
                ('albums', models.ManyToManyField(through='api.AlbumSongs', to='api.album', verbose_name='Альбомы')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
        migrations.AddField(
            model_name='albumsongs',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_songs', to='api.song', verbose_name='Название песни'),
        ),
        migrations.AddField(
            model_name='album',
            name='music_performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.musicperformer', verbose_name='Музыкальный исполнитель'),
        ),
        migrations.AddConstraint(
            model_name='albumsongs',
            constraint=models.UniqueConstraint(fields=('album', 'song'), name='unique_albums_song'),
        ),
        migrations.AddConstraint(
            model_name='albumsongs',
            constraint=models.UniqueConstraint(fields=('serial_number', 'song'), name='unique_songs_serial_number'),
        ),
    ]