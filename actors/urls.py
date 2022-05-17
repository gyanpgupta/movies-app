from django.urls import path

from . import views

urlpatterns = [
    path("api/actors/", views.PersonListCreateAPIView.as_view(), name="person"),
    path(
        "api/actors/<int:id>/",
        views.PersonDetailAPIView.as_view(),
        name="person_detail",
    ),
]
