from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Movie, Genre, Tag

# Create your views here.
def home_page(request):
    featured_movies = Movie.objects.filter(deleted=False).order_by('-releasedate')[:5]
    top_rated_movies = Movie.objects.filter(deleted=False).order_by('-rating')[:5]
    recent_movies = Movie.objects.filter(deleted=False).order_by('-movieid')[:5]
    genres = Genre.objects.all()
    popular_tags = Tag.objects.all()[:5]  

    context = {
        'featured_movies': featured_movies,
        'top_rated_movies': top_rated_movies,
        'recent_movies': recent_movies,
        'genres': genres,
        'popular_tags': popular_tags,
    }

    return render(request, 'home_page.html', context)

class TopRatedPage(TemplateView):
    # Specify the templates to display
    template_name = 'toprated.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        top_rated_movies = Movie.objects.filter(deleted=False).order_by('-rating')
        context['top_rated_movies'] = top_rated_movies
        return context

def movies_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = Movie.objects.filter(genres=genre, deleted=False)
    context = {
        'genre': genre,
        'movies': movies,
    }
    return render(request, 'movies_by_genre.html', context)

def search_movies(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(title__icontains=query, deleted=False)
    context = {
        'query': query,
        'movies': movies,
    }
    return render(request, 'search_results.html', context)

def movies_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    movies = Movie.objects.filter(tags=tag, deleted=False)
    context = {
        'tag': tag,
        'movies': movies,
    }
    return render(request, 'movies_by_tag.html', context)
