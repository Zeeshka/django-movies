from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movies.html'


class MovieDetailView(DetailView):
    # Описание фильмов
    model = Movie
    slug_field = "url"
    template_name = 'movie_detail.html'

class AddReview(View):
    # Отзывы
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            parent_comment_id = request.POST.get('contactparent', None)
            if parent_comment_id:
                comment.parent_id = parent_comment_id
                comment.save()
        return redirect(movie.get_absolute_url())