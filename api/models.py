from django.db import models
# importeren van ModelResource van tastypie
from tastypie.resources import ModelResource
# importeren van het Movie model die staat in movies/models.py
from movies.models import Movie

# Definiëren van een API resource voor het Movie model


class MovieResource(ModelResource):
    class Meta:
        # Alle Movie objecten beschikbaar maken via de API
        queryset = Movie.objects.all()
        resource_name = 'movies'  # Naam van de resource in de API
        # Velden die niet in de API response moeten verschijnen
        excludes = ['date_created']
