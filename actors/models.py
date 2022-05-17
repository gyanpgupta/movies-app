from datetime import datetime
from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.died:
            return "{}, {} ({}-{})".format(
                self.last_name,
                self.first_name,
                datetime.date.strftime(self.born, "%d/%m/%Y"),
                datetime.date.strftime(self.died, "%d/%m/%Y"),
            )
        return "{}, {} ({})".format(
            self.last_name,
            self.first_name,
            datetime.date.strftime(self.born, "%d/%m/%Y"),
        )
