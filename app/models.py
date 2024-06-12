# app/models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    city = Column(String)
    coach_id = Column(Integer, ForeignKey("coaches.id"))

    coach = relationship("Coach", back_populates="team")
    players = relationship("Player", back_populates="team")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="players")

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    location = Column(String)
    home_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))

    home_team = relationship("Team", foreign_keys=[home_team_id], backref="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], backref="away_matches")

class Coach(Base):
    __tablename__ = "coaches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    team = relationship("Team", back_populates="coach")
