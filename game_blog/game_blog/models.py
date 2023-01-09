from django.db import models
from datetime import date


class Platform(models.Model):

    name = models.CharField(
        max_length=200,
        default='PC',
        )
    
    def __str__(self):
        return self.name

class Genre(models.Model):

    name = models.CharField(
        max_length=200,
        default='Action',
    )

    def __str__(self):
        return self.name

class Game(models.Model):

    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    # platform = models.ManyToManyField(
    #     Platform,
    #     choices=[tuple([x,x]) for x in Platform.objects.all()]
    # )
    # genre = models.ManyToManyField(
    #     Genre,
    #     choices=[tuple([x,x]) for x in Genre.objects.all()]
    # )

    #//// Still giving field 'id' value issues, keeps trying to use first letter of selected platform instead of id

    RELEASE_YEAR_CHOICES = [tuple([x,x]) for x in range(date.today().year, 2000, -1)]
    release_year = models.IntegerField(
        choices=RELEASE_YEAR_CHOICES,
    )
    RATING_CHOICES=[tuple([x,x]) for x in range(10, 0, -1)]
    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )
    description = models.TextField()
    review = models.TextField()