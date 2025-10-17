from django.contrib import admin  # importeren van de admin module
from .models import Movie, Genre  # importeren van de Movie en Genre modellen


class GenreAdmin(admin.ModelAdmin):  # Aangepaste admin weergave voor het Genre model
    # Weergave van id en naam in de admin lijstweergave
    list_display = ('id', 'name',)


class MovieAdmin(admin.ModelAdmin):  # Aangepaste admin weergave voor het Movie model
    # Uitsluiten van het date_created veld in de admin interface
    exclude = ('date_created',)
    # Weergave van titel, aantal op voorraad en dagelijkse prijs in de admin lijstweergave
    list_display = ('title', 'number_in_stock', 'daily_rate')


# Register your models here.
# Registreren van het Movie model met aangepaste admin weergave
admin.site.register(Movie, MovieAdmin)
# Registreren van het Genre model met aangepaste admin weergave
admin.site.register(Genre, GenreAdmin)
# Hierdoor kunnen we films en genres beheren via de Django admin interface
