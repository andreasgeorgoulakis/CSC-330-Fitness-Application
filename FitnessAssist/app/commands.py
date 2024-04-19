from app import app, db
from app.models import FitnessChallenge
from datetime import datetime, timedelta

app.app_context().push()

def populate_fitness_challenges():
    challenges = [
        {"name": "Mile Run", "description": "Run a mile every day", "link": ""},
        {"name": "Push-ups", "description": "Do 20 push-ups every day", "link": ""},
        {"name": "Squats", "description": "Do 30 squats every day", "link": ""},
        {"name": "Plank", "description": "Hold a plank for 30 seconds every day", "link": ""},
        {"name": "Yoga", "description": "Follow a 10-minute yoga routine every day", "link": "https://youtu.be/SvPKFsCiMsw?si=bG2VlnlFFkRsXCdH"},
        {"name": "Jumping Jacks", "description": "Do 50 jumping jacks every day", "link": ""},
        {"name": "Sit-ups", "description": "Do 20 sit-ups every day", "link": ""},
        {"name": "Lunges", "description": "Do 30 lunges every day", "link": ""},
        {"name": "Cycling", "description": "Cycle for 10 minutes every day", "link": ""},
        {"name": "Swimming", "description": "Swim for 10 minutes every day", "link": ""},
        {"name": "Dumbbell Rows", "description": "Do 20 dumbbell rows every day", "link": "https://youtu.be/dFzUjzfih7k?si=tbGXR8mGJPoRI0tC"},
        {"name": "Burpees", "description": "Do 10 burpees every day", "link": "https://youtu.be/r6MBg8-FlD4?si=e1uO0cukOTkH8LRz"},
        {"name": "Mountain Climbers", "description": "Do 30 mountain climbers every day", "link": ""},
        {"name": "Leg Raises", "description": "Do 20 leg raises every day", "link": ""},
        {"name": "Wall Sit", "description": "Hold a wall sit for 30 seconds every day", "link": ""},
        {"name": "Calf Raises", "description": "Do 30 calf raises every day", "link": ""},
        {"name": "Russian Twists", "description": "Do 20 Russian twists every day", "link": ""},
        {"name": "Tricep Dips", "description": "Do 20 tricep dips every day", "link": ""},
        {"name": "Bicep Curls", "description": "Do 20 bicep curls every day", "link": ""},
        {"name": "Jump Rope", "description": "Jump rope for 10 minutes every day", "link": ""},
        {"name": "Kettlebell Swings", "description": "Do 20 kettlebell swings every day", "link": "https://youtu.be/DqkYuWR4zRI?si=l12ALlNXgJptyOOH"},
        {"name": "Box Jumps", "description": "Do 20 box jumps every day", "link": ""},
        {"name": "Battle Ropes", "description": "Do 20 battle ropes every day", "link": ""},
        {"name": "Plyometric Lunges", "description": "Do 20 plyometric lunges every day", "link": ""},
        {"name": "Side Plank", "description": "Hold a side plank for 30 seconds every day", "link": ""},
        {"name": "Glute Bridges", "description": "Do 20 glute bridges every day", "link": ""},
        {"name": "Step-ups", "description": "Do 20 step-ups every day", "link": ""},
        {"name": "Chest Press", "description": "Do 20 chest presses every day", "link": ""},
        {"name": "Lat Pulldowns", "description": "Do 5 sets of low weight, slow and controlled reps", "link": ""},
        {"name": "Shoulder Press", "description": "Do 4 sets of 10", "link": "https://youtu.be/5yWaNOvgFCM?si=tugw8if0HE5k1poI"},
    ]

    for challenge in challenges:
        # Create a new challenge every 24 hours
        for i in range(30):
            challenge_date = datetime.now() + timedelta(days=i)
            db.session.add(FitnessChallenge(**challenge, created_at=challenge_date))
    db.session.commit()

if __name__ == "__main__":
    populate_fitness_challenges()