from django.db import models

class LocationManager(models.Manager):
    def get_location_by_country(self, country):
        return super().get_queryset().filter(location_country=country)
    
    def get_location_by_city(self, city):
        return super().get_queryset().filter(location_city=city)
    
    def get_location_by_name(self, name):
        return super().get_queryset().filter(location_name=name)

class Location(models.Model):
    location_name = models.CharField(max_length=100, blank=False, null=False)
    location_address = models.CharField(max_length=250, blank=False, null=False)
    location_city = models.CharField(max_length=100, blank=False, null=False)
    location_state = models.CharField(max_length=100, blank=False, null=False)
    location_country = models.CharField(max_length=100, blank=False, null=False)
    location_capacity = models.IntegerField(default=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    local_objects = LocationManager()

    class Meta:
        ordering = ['location_name']
        indexes = [
            models.Index(fields=['location_city','location_country'])
        ]
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return f"{self.location_name} - {self.location_country}"
