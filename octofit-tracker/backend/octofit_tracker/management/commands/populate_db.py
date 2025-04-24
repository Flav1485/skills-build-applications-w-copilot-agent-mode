from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "user1@example.com", "name": "User One", "team": "Team A"},
            {"email": "user2@example.com", "name": "User Two", "team": "Team B"},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team A", "members": ["user1@example.com"]},
            {"name": "Team B", "members": ["user2@example.com"]},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"activity_id": 1, "name": "Running", "calories_burned": 300},
            {"activity_id": 2, "name": "Cycling", "calories_burned": 250},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"leaderboard_id": 1, "user": "user1@example.com", "points": 100},
            {"leaderboard_id": 2, "user": "user2@example.com", "points": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"workout_id": 1, "user": "user1@example.com", "activity": "Running", "duration": 30},
            {"workout_id": 2, "user": "user2@example.com", "activity": "Cycling", "duration": 45},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
