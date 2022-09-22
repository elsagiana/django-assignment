from django.db import models

# Create your models here.
class WatchList(models.Model):
    watched = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()