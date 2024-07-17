from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Movie

# Create your views here.
def home_page(request):
    featured_movies = Movie.objects.filter(deleted=False).order_by('-releasedate')

    movies_list = "".join([f"<li>{movie.title} ({movie.releaseyear})</li>" for movie in featured_movies])

    response = f"""
        <html>
            <h1>Welcome to MyMovies App</h1>
            <h2>Featured Movies</h2>
            <ul>
                {movies_list}
            </ul>
        </html>
    """

    return HttpResponse(response)

class TopRatedPage(TemplateView):
    # Specify the templates to display
    template_name = 'toprated.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        top_rated_movies = Movie.objects.filter(deleted=False).order_by('-rating')
        context['top_rated_movies'] = top_rated_movies
        return context
