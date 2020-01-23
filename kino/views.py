from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    # Список фильмов
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'website/movies.html', {'movie_list': movies})


class MovieDetailView(View):
    # Описание фильмов
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "website/movie_detail.html", {'movie': movie})