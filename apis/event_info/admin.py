from django.contrib import admin
from .models.artist import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['artist_country', 'artist_name']
    list_display = [
        'artist_name',
        'artist_country',
        'artist_image',
        'created_at',
        'updated_at'
    ]
