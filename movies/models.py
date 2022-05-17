from django.db import models

from actors.models import Person

# Create your models here.


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_PG13 = 3
    RATED_R = 4
    RATED_NC17 = 5
    RATINGS = (
        (NOT_RATED, "NR - Not Rate"),
        (RATED_G, "G - General Audiences"),
        (RATED_PG, "PG – Parental Guidance Suggested"),
        (RATED_PG13, "PG-13 – Parents Strongly Cautioned"),
        (RATED_R, "R – Restricted"),
        (RATED_NC17, "NC-17 – Adults Only"),
    )

    title = models.CharField(max_length=255)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    actors = models.ManyToManyField(Person, related_name="acting_credits", blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
