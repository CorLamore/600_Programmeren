# importeren van render om HTML templates te renderen
from django.shortcuts import render


def home(request):  # View functie voor de home pagina
    return render(request, 'home.html', {})
