"""
URL configuration for vidly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# importeren van de classe MovieResource uit api/models.py
from api.models import MovieResource
from . import views  # importeren van de views uit de huidige map

movie_resource = MovieResource()  # Is de instantie van MovieResource

urlpatterns = [
    path('', views.home),  # Home pagina route
    path('admin/', admin.site.urls),
    # Include the URLs from the movies app
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls)),  # toevoegen van de API URLs
]
