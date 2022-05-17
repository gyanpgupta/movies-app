from actors.serializers import PersonSerializer
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "plot",
            "year",
            "rating",
            "runtime",
            "website",
            "actors",
        ]
