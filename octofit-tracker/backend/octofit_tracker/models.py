from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    """Custom field to handle MongoDB ObjectId."""
    def get_prep_value(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

class User(models.Model):
    id = ObjectIdField(primary_key=True)  # Use ObjectId as the primary key
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.JSONField()

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()