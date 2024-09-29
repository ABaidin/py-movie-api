from django.urls import path

from cinema import views

urlpatterns = [
    path("movies/", views.movie_list, name="movies"),
    path("movies/<int:pk>/", views.movie_detail, name="movie-detail"),
]

app_name = "cinema"