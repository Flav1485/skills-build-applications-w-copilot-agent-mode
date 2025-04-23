# models.py

from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    # ...other fields...

class Team(models.Model):
    name = models.CharField(max_length=100)
    # ...other fields...

class Activity(models.Model):
    description = models.TextField()
    # ...other fields...

class Leaderboard(models.Model):
    rank = models.IntegerField()
    # ...other fields...

class Workout(models.Model):
    type = models.CharField(max_length=100)
    # ...other fields...
