from django.urls import path  # De path functie importeren uit django.urls
from . import views  # De views importeren uit de huidige map

app_name = 'movies'  # De app_name instellen voor namespacing van URL-namen

urlpatterns = [
    # De URL-patronen definiëren
    # De root URL koppelen aan de index view
    path('', views.movie_index, name='index'),  # '' betekent de root URL
    # URL met een integer parameter voor movie_id
    # path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/', views.movie_detail, name='detail'),
    # path('another/', views.another_view, name='another') # Een voorbeeld van een andere URL
]
