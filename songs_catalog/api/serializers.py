from .models import Album, AlbumSongs, MusicPerformer
from rest_framework import serializers


class AlbumSongsSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField()
    class Meta:
        model = AlbumSongs
        fields = (
            'serial_number',
            'song'            
        )


class AllAlbumsSerializer(serializers.ModelSerializer):
    music_performer = serializers.StringRelatedField()
    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'music_performer',
            'release_year'
        )


class AlbumSerializer(serializers.ModelSerializer):
    album_songs = AlbumSongsSerializer(many=True)
    music_performer = serializers.StringRelatedField()
    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'music_performer',
            'release_year',
            'album_songs'
        )


class AllPerformersAlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'release_year'
        )


class PerformerSerializer(serializers.ModelSerializer):
    albums = AllPerformersAlbumsSerializer(many=True)
    class Meta:
        model = MusicPerformer
        fields = (
            'id',
            'name',
            'albums'
        )


class AllPerformersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPerformer
        fields = (
            'id',
            'name'
        )