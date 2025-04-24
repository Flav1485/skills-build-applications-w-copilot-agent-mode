# Test data for OctoFit Tracker

test_data = {
    "users": [
        {"email": "student1@school.com", "name": "Student One", "team": "Team Alpha"},
        {"email": "student2@school.com", "name": "Student Two", "team": "Team Beta"},
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["student1@school.com"]},
        {"name": "Team Beta", "members": ["student2@school.com"]},
    ],
    "activities": [
        {"activity_id": 1, "name": "Basketball", "calories_burned": 500},
        {"activity_id": 2, "name": "Soccer", "calories_burned": 450},
    ],
    "leaderboard": [
        {"leaderboard_id": 1, "user": "student1@school.com", "points": 120},
        {"leaderboard_id": 2, "user": "student2@school.com", "points": 100},
    ],
    "workouts": [
        {
            "workout_id": 1,
            "user": "student1@school.com",
            "activity": "Basketball",
            "duration": 60,
        },
        {
            "workout_id": 2,
            "user": "student2@school.com",
            "activity": "Soccer",
            "duration": 45,
        },
    ],
}
