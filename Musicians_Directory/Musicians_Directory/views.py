from django.shortcuts import render
from musicians.models import Musician
def homepage(request):
    data = Musician.objects.all()
    return render(request, 'homepage.html', {'data' : data})

