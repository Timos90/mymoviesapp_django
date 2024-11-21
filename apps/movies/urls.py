from django.urls import path
from . import views

app_name = 'movies-urls'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('top-rated/', views.TopRatedPage.as_view(), name='top_rated'),
    path('genre/<int:genre_id>/', views.movies_by_genre, name='movies_by_genre'),
    path('tag/<int:tag_id>/', views.movies_by_tag, name='movies_by_tag'),
    path('search/', views.search_movies, name='search_movies'),
]
