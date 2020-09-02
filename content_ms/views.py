from django.shortcuts import render
from .models import Genre

def show_genres(request):
    return render(request, "genre.html", {'genres': Genre.objects.all()})