# tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'}
        response = self.client.post('/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        data = {'name': 'Team A', 'members': []}
        response = self.client.post('/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password123')
        data = {'user': user.id, 'activity_type': 'Running', 'duration': 30, 'date': '2025-04-24'}
        response = self.client.post('/activities/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Team A')
        data = {'team': team.id, 'points': 100}
        response = self.client.post('/leaderboard/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        data = {'name': 'Workout A', 'description': 'Test workout', 'duration': 60}
        response = self.client.post('/workouts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
