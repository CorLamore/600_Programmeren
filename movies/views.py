from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie  # importeren van het Movie model

# Create your views here.


def movie_index(request):
    # # Voorbeeld van het gebruik van de Movie model om database queries uit te voeren
    # Movie.objects.all()  # Ophalen van alle Movie objecten uit de database
    # # SELECT * FROM movies_movie; (Django ORM query)
    # # Filteren van Movie objecten op release_year
    #  Movie.objects.filter(release_year=1984)
    # # SELECT * FROM movies_movie WHERE release_year=1984; (Django ORM query)
    # # Renderen van een eenvoudige HttpResponse
    # return HttpResponse("Hello, world. You're at the movies index.")

    # # Om een lijst zichtbaar te maken in de browser
    # # Ophalen van alle Movie objecten uit de database
    # movies_ophalen = Movie.objects.all()
    # # Comma-separated list of movie titles
    # output = ', '.join([m.title for m in movies_ophalen])
    # return HttpResponse(output)

    # # Renderen van een HTML template met de lijst van films
    # Ophalen van alle Movie objecten uit de database
    movies_ophalen = Movie.objects.all()
    # Renderen van de 'index.html' template met de context {'movies': movies_ophalen}
    # return render(request, 'index.html', {'movies': movies_ophalen})
    return render(request, 'movies/movie_index.html', {'movies': movies_ophalen})


# View functie voor het weergeven van details van een specifieke film
def movie_detail(request, movie_id):
    # try:  # Try-except block om te controleren of het Movie object bestaat
    #     # Ophalen van een specifiek Movie object op basis van movie_id
    #     film_id = Movie.objects.get(id=movie_id)
    #     return render(request, 'movies/movie_detail.html', {'movie': film_id})
    # except Movie.DoesNotExist:
    #     return HttpResponse("Movie not found.", status=404)
    #     # raise Http404("Movie not found.") # Raise a 404 error if the movie does not exist

    # Ophalen van een specifiek Movie object op basis van movie_id
    # Gebruik van get_object_or_404 om een 404 error te genereren als het object niet bestaat
    film_id = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': film_id})
