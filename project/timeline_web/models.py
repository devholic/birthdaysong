from django.db import models

# Create your models here.
class Rankdata(models.Model):
	chart = models.TextField()
	year = models.PositiveSmallIntegerField()
	week = models.PositiveSmallIntegerField()
	title = models.TextField()
	artist = models.TextField()
	album = models.TextField()
	youtube = models.TextField()
