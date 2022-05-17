from actors.models import Person
from actors.serializers import PersonSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class PersonListCreateAPIView(generics.ListCreateAPIView):
    """
    Person/Actor List Api View, It will return the persons/actors list or create a person/actor
    """

    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = [DjangoFilterBackend]


class PersonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Person/Actor Detail Api View, It will return a single person/actor or will update, delete a person/actor
    """

    serializer_class = PersonSerializer
    lookup_url_kwarg = "id"
    queryset = Person.objects.all()
