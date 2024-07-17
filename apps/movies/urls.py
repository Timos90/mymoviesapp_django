from django.urls import path
from . import views

app_name = 'movies-urls'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('top-rated/', views.TopRatedPage.as_view(), name='top-rated-movies'),
]
