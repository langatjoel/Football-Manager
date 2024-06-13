# app/helpers.py

from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Team, Player

def create_team(name: str, city: str):
    db = SessionLocal()
    team = Team(name=name, city=city)
    db.add(team)
    db.commit()
    db.close()

def create_player(name: str, position: str, team_id: int):
    db = SessionLocal()
    player = Player(name=name, position=position, team_id=team_id)
    db.add(player)
    db.commit()
    db.close()

def list_teams():
    db = SessionLocal()
    teams = db.query(Team).all()
    for team in teams:
        print(f"ID: {team.id}, Name: {team.name}, City: {team.city}")
    db.close()

def list_players():
    db = SessionLocal()
    players = db.query(Player).all()
    for player in players:
        print(f"ID: {player.id}, Name: {player.name}, Position: {player.position}, Team ID: {player.team_id}")
    db.close()

def find_team_by_name(name: str):
    db = SessionLocal()
    team = db.query(Team).filter(Team.name == name).first()
    if team:
        print(f"ID: {team.id}, Name: {team.name}, City: {team.city}")
    else:
        print(f"Team '{name}' not found.")
    db.close()

def find_player_by_name(name: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.name == name).first()
    if player:
        print(f"ID: {player.id}, Name: {player.name}, Position: {player.position}, Team ID: {player.team_id}")
    else:
        print(f"Player '{name}' not found.")
    db.close()

def exit_program():
    print("Exiting program.")
    exit()
