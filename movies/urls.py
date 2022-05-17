from django.urls import path

from . import views

urlpatterns = [
    path("api/movies/", views.MovieAPIView.as_view(), name="movies"),
    path(
        "api/movies/<int:id>/", views.MovieDetailAPIView.as_view(), name="movie_deatil"
    ),
]
