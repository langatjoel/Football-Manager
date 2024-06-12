# app/helpers.py
from sqlalchemy.orm import Session
from app.db import SessionLocal, init_db
from app.models import Team, Player, Match, Coach

def init_database():
    init_db()
    print("Initialized the database.")

def create_team(name, city, coach_name):
    db: Session = SessionLocal()
    coach = Coach(name=coach_name)
    team = Team(name=name, city=city, coach=coach)
    db.add(team)
    db.commit()
    db.close()
    print(f"Created team {name} in {city} with coach {coach_name}.")

def create_player(name, position, team_id):
    db: Session = SessionLocal()
    player = Player(name=name, position=position, team_id=team_id)
    db.add(player)
    db.commit()
    db.close()
    print(f"Created player {name} as {position} in team {team_id}.")

def create_match(date, location, home_team_id, away_team_id):
    db: Session = SessionLocal()
    match = Match(date=date, location=location, home_team_id=home_team_id, away_team_id=away_team_id)
    db.add(match)
    db.commit()
    db.close()
    print(f"Created match on {date} at {location} between teams {home_team_id} and {away_team_id}.")

def exit_program():
    print("Goodbye!")
    exit()
