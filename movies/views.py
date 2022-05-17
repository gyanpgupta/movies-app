from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies.serializers import MovieSerializer


# Create your views here.


class MovieAPIView(APIView):
    def get(self, request):
        """Get/Filter api for movies List

        :param request: Request object
        """
        movies = Movie.objects.all()
        if request.query_params.get("title"):
            title = request.query_params["title"]
            movies = Movie.objects.filter(title__exact=title)
            movies = [movie for movie in movies if movie.title == title]
        serlizer = MovieSerializer(movies, many=True)
        return Response(serlizer.data, status.HTTP_200_OK)

    def post(self, request):
        """Post api for creating a movie

        :param request: Request object
        """
        serlizer = MovieSerializer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data, status=status.HTTP_201_CREATED)
        return Response(serlizer.errors, status=status.HTTP_404_NOT_FOUND)


class MovieDetailAPIView(APIView):
    def get(self, request, id):
        """Get api for returning a single movie

        :param request: Request object
        :param id: movie id
        """
        movie = get_object_or_404(Movie, pk=id)
        serlizer = MovieSerializer(movie)
        return Response(serlizer.data, status.HTTP_200_OK)

    def put(self, request, id):
        """Update api for updating a single movie

        :param request: Request object
        :param id: movie id
        """
        movie = get_object_or_404(Movie, pk=id)
        serlizer = MovieSerializer(movie)
        return Response(serlizer.data, status.HTTP_200_OK)
