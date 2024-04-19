from app import app, db
from app.models import FitnessChallenge, User
from datetime import datetime, timedelta

app.app_context().push()

def populate_fitness_challenges():
    challenges = [
        {"name": "Mile Run", "description": "Run a mile every day", "link": "https://youtu.be/9D-QD_HIfjA?si=zR0BTZkumaCAx-F7"},
        {"name": "Push-ups", "description": "Do 20 push-ups every day", "link": "https://youtu.be/JyCG_5l3XLk?si=thDjxUesTJtpUz66"},
        {"name": "Squats", "description": "Hold a squat for 3 mins", "link": "https://youtu.be/IB_icWRzi4E?si=LYwn8PpFFqwun3cf"},
        {"name": "Plank", "description": "Hold a plank for 30 seconds every day", "link": "https://youtu.be/yeKv5oX_6GY?si=doOZIzxpeTsdNxpc"},
        {"name": "Yoga", "description": "Follow a 10-minute yoga routine", "link": "https://youtu.be/SvPKFsCiMsw?si=bG2VlnlFFkRsXCdH"},
        {"name": "Jumping Jacks", "description": "Do 100 jumping jacks", "link": "https://youtu.be/yDSMdd8hiFg?si=3KkmCNRrwF-1TfTo"},
        {"name": "Sit-ups", "description": "Do 30 sit-ups", "link": "https://youtu.be/jDwoBqPH0jk?si=kZgIDDGKSH0IFti7"},
        {"name": "Lunges", "description": "Do 50 (25 each leg) lunges", "link": "https://youtu.be/3XDriUn0udo?si=PnmmRY_fIHLbP6kv"},
        {"name": "Cycling", "description": "Cycle for 10 minutes. You can use a machine too.", "link": "https://youtu.be/QJ_I9sXosFg?si=F5yjuqSPgKd-1uxy"},
        {"name": "Jog in place", "description": "Jog in place for 5 mins.", "link": "https://youtu.be/hBU28Wd4Hf8?si=vzzzpqduMtN3zELJ"},
        {"name": "Dumbbell Rows", "description": "Do 20 dumbbell rows every day", "link": "https://youtu.be/dFzUjzfih7k?si=tbGXR8mGJPoRI0tC"},
        {"name": "Burpees", "description": "Do 10 burpees every day", "link": "https://youtu.be/r6MBg8-FlD4?si=e1uO0cukOTkH8LRz"},
        {"name": "Mountain Climbers", "description": "Do mountain climbers for 2 minutes. Pause if you need but you must total 120 seconds!", "link": "https://youtu.be/De3Gl-nC7IQ?si=p7e8fFpyV7-b2hxf"},
        {"name": "Leg Raises", "description": "Do 30 (15 each leg) slow and controlled leg raises", "link": "https://youtu.be/JMsqY_UegbM?si=Il7eOJvzRVx71i29"},
        {"name": "Wall Sit", "description": "Hold a wall sit for 45 seconds. Do this twice. Do it with a heavy book in your lip if it's too easy!", "link": "https://youtu.be/eb7vLD6V-iU?si=FX-V7aR-82GWKcIH"},
        {"name": "Calf Raises", "description": "Do 60 calf raises.", "link": "https://youtu.be/eMTy3qylqnE?si=tG9hcDoaA1xWeG3S"},
        {"name": "Russian Twists", "description": "Do Russian twists for a minute and a half.", "link": "https://youtu.be/VfWoNC-NMII?si=N02oOh4OXGw62DyO"},
        {"name": "Tricep Dips", "description": "Do 30 tricep dips. Feel the burn.", "link": "https://youtu.be/0326dy_-CzM?si=FX2EAuODbh7eRQoD"},
        {"name": "Bicep Curls", "description": "Do 50 bicep curls. You can space these out!", "link": "https://youtu.be/ykJmrZ5v0Oo?si=lmlJf1gK5F3r45Yn"},
        {"name": "Jump Rope", "description": "Jump rope for 10 minutes every day", "link": "https://youtu.be/MqUhcwDV_fc?si=PWOiDVKQqN0EOZq6"},
        {"name": "Kettlebell Swings", "description": "Do 20 kettlebell swings every day", "link": "https://youtu.be/DqkYuWR4zRI?si=l12ALlNXgJptyOOH"},
        {"name": "Box Jumps", "description": "Do 20 box jumps", "link": "https://youtu.be/kNIInK_Le8I?si=Mr4EA_oopNlDrRj9"},
        {"name": "Battle Ropes", "description": "Do battle ropes for 2 minutes.", "link": "https://youtu.be/1gNMRV1GUFg?si=DE6KFsY9MCvtZ8FT"},
        {"name": "Plyometric Lunges", "description": "Do plyometric lunges for 1 minute straight. Do that twice.", "link": "https://youtu.be/PZPSz905Ovk?si=Yn4bGJXgARFFR2Kr"},
        {"name": "Side Plank", "description": "Hold a side plank for 30 seconds. Can you do both sides?", "link": "https://youtu.be/9dNL_mtObGQ?si=x_dGFJp9qDPZTEb4"},
        {"name": "Glute Bridges", "description": "Do 30 glute bridges", "link": "https://youtu.be/OUgsJ8-Vi0E?si=XPup7uF94H7aaQnK"},
        {"name": "Step-ups", "description": "Do 40 (20 each leg) step-ups", "link": "https://youtu.be/9ZknEYboBOQ?si=uT1v4dA2sBSy41OM"},
        {"name": "Chest Press", "description": "Do 20-25 reps of low weight for two sets, then on the last set go until failure", "link": "https://youtu.be/VmB1G1K7v94?si=9v5zwuiGV0GOfSw4"},
        {"name": "Lat Pulldowns", "description": "Do 5 sets of 10 with low weight and slow + controlled reps", "link": "https://youtu.be/trZQjegcRx0?si=SQKQ9aigqgj83-a9"},
        {"name": "Shoulder Press", "description": "Do 4 sets of 10 reps", "link": "https://youtu.be/5yWaNOvgFCM?si=tugw8if0HE5k1poI"},
    ]

    for challenge in challenges:
        # Create a new challenge every 24 hours
        for i in range(30):
            challenge_date = datetime.now() + timedelta(days=i)
            db.session.add(FitnessChallenge(**challenge, created_at=challenge_date))
    db.session.commit()

def complete_challenge(challenge_id):
    challenge = FitnessChallenge.query.get(challenge_id)
    if challenge:
        challenge.completed = True
        db.session.commit()
        user = challenge.user
        user.challenges_completed_in_row += 1
        user.total_challenges_completed += 1
        db.session.commit()

def reset_streak(user_id):
    user = User.query.get(user_id)
    if user:
        user.challenges_completed_in_row = 0
        db.session.commit()

if __name__ == "__main__":
    populate_fitness_challenges()