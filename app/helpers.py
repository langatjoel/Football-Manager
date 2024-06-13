# app/helpers.py

from sqlalchemy.orm import Session
from app.models import Team, Player, Coach, Match
from app.db import SessionLocal, init_db

def init_database():
    init_db()

def create_team(name, city, coach_name):
    db = SessionLocal()
    new_team = Team(name=name, city=city)
    db.add(new_team)
    db.commit()
    new_coach = Coach(name=coach_name, team_id=new_team.id)
    db.add(new_coach)
    db.commit()
    db.close()

def create_coach(name, team_id):
    db = SessionLocal()
    new_coach = Coach(name=name, team_id=team_id)
    db.add(new_coach)
    db.commit()
    db.close()

def create_player(name, position, team_id):
    db = SessionLocal()
    new_player = Player(name=name, position=position, team_id=team_id)
    db.add(new_player)
    db.commit()
    db.close()

def create_match(date, location, home_team_id, away_team_id):
    db = SessionLocal()
    new_match = Match(date=date, location=location, home_team_id=home_team_id, away_team_id=away_team_id)
    db.add(new_match)
    db.commit()
    db.close()

def list_teams():
    db = SessionLocal()
    teams = db.query(Team).all()
    for team in teams:
        print(f"ID: {team.id}, Name: {team.name}, City: {team.city}, Coach: {team.coach.name if team.coach else 'None'}")
    db.close()

def list_coaches():
    db = SessionLocal()
    coaches = db.query(Coach).all()
    for coach in coaches:
        print(f"ID: {coach.id}, Name: {coach.name}, Team: {coach.team.name if coach.team else 'None'}")
    db.close()

def list_players():
    db = SessionLocal()
    players = db.query(Player).all()
    for player in players:
        print(f"ID: {player.id}, Name: {player.name}, Position: {player.position}, Team: {player.team.name if player.team else 'None'}")
    db.close()

def find_team_by_name(name):
    db = SessionLocal()
    team = db.query(Team).filter(Team.name == name).first()
    if team:
        print(f"ID: {team.id}, Name: {team.name}, City: {team.city}, Coach: {team.coach.name if team.coach else 'None'}")
    else:
        print("Team not found.")
    db.close()

def find_player_by_name(name):
    db = SessionLocal()
    player = db.query(Player).filter(Player.name == name).first()
    if player:
        print(f"ID: {player.id}, Name: {player.name}, Position: {player.position}, Team: {player.team.name if player.team else 'None'}")
    else:
        print("Player not found.")
    db.close()

def find_coach_by_name(name):
    db = SessionLocal()
    coach = db.query(Coach).filter(Coach.name == name).first()
    if coach:
        print(f"ID: {coach.id}, Name: {coach.name}, Team: {coach.team.name if coach.team else 'None'}")
    else:
        print("Coach not found.")
    db.close()

def exit_program():
    print("Goodbye!")
    exit()
