from django.db import models
from django.db.models import Manager
from cloudinary.models import CloudinaryField

class ArtistManager(models.Manager):
    def get_artist_by_name(self, name):
        return super().get_queryset().filter(artist_name=name)
    
    def get_artist_by_country(self, country):
        return super().get_queryset().filter(artist_country=country)

class Artist(models.Model):
    artist_name = models.CharField(max_length=100, blank=False, null=False)
    artist_country = models.CharField(max_length=100, blank=False, null=False)
    artist_bio = models.TextField(blank=True, null=True)
    artist_image = CloudinaryField('image', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    artist_objects = ArtistManager()

    class Meta:
        ordering = ['artist_name']
        indexes = [
            models.Index(fields=['-created_at', 'artist_country'])
        ]
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return f'{self.artist_name} - {self.artist_country}'
