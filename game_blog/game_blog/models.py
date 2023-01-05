from django.db import models
from datetime import date

class Game(models.Model):
    title = models.CharField(max_length=200)
    # GENRE_CHOICES = [tuple(['ACTION', 'Action'], ['ACTION_ADVENTURE', 'Action-Adventure'], ['ADVENTURE', 'Adventure'], ['PUZZLE', 'Puzzle'], ['ROLE_PLAYING', 'Role-Playing'], ['SIMULATION', 'Simulation'], ['STRATEGY', 'Strategy'], ['SPORTS', 'Sports'], ['MMO', 'MMO'])]
    # genre = models.CharField(
    #     max_length=50,
    #     choices=GENRE_CHOICES,
    #     default='Action',
    # )
    RELEASE_YEAR_CHOICES = [tuple([x,x]) for x in range(date.today().year, 2000, -1)]
    release_year = models.CharField(
        max_length=4,
        choices=RELEASE_YEAR_CHOICES,
        default=date.today().year,
    )
    RATING_CHOICES=[tuple([x,x]) for x in range(10, 0, -1)]
    rating = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default=10,
    )
    description = models.TextField()
    review = models.TextField()