from django.db import models  # Import the models module from django.db
from django.utils import timezone  # Import timezone utility from django.utils


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)  # Name field for the genre

    def __str__(self):
        return self.name  # String representation of the Genre model


class Movie(models.Model):
    title = models.CharField(max_length=255)  # Title field for the movie
    release_year = models.IntegerField()  # Release year field for the movie
    number_in_stock = models.IntegerField()  # Number in stock field for the movie
    daily_rate = models.FloatField()  # Daily rate field for the movie
    # Foreign key to Genre model
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # date_created = models.DateTimeField(auto_now_add=True )  # Date created field for the movie
    # Date created field for the movie
    date_created = models.DateTimeField(default=timezone.now)  # auto_now=True
