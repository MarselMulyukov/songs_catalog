from django.contrib import admin
from .models import Album, AlbumSongs, MusicPerformer, Song


class SongsInline(admin.TabularInline):
    model = AlbumSongs


class AlbumInline(admin.TabularInline):
    model = Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'music_performer', 'release_year')
    list_filter = ('music_performer', 'release_year')
    inlines = (SongsInline,)
    fields = ('title', 'music_performer', 'release_year')


class SongAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('albums', 'albums__music_performer')
    inlines = (SongsInline,)


class MusicPerformerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (AlbumInline,)
    fields = ('name',)


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(MusicPerformer, MusicPerformerAdmin)
