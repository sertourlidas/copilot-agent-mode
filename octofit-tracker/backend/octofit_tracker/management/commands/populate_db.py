from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)  # Connect to MongoDB running locally
        db = client['octofit_db']  # Use the correct database name
        

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Add test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith")

        # Add test teams
        team1 = Team.objects.create(name="Team Alpha", members=[str(user1.id), str(user2.id)])

        # Add test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Add test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Add test workouts
        Workout.objects.create(name="Morning Run", description="A 5km run to start the day.")
        Workout.objects.create(name="Evening Yoga", description="A relaxing yoga session.")

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))