# Football Manager CLI Application

## Overview
The Football Manager CLI application allows users to manage football teams, players, matches, and coaches. It leverages SQLAlchemy for ORM and Click for creating the command-line interface.

## Features
- Initialize the database
- Create teams
- Create players
- Create matches
- Assign coaches to teams
- List teams, players, and matches

## Project Structure
football_manager/
├── app/
│ ├── init.py
│ ├── cli.py
│ ├── models.py
│ ├── db.py
├── Pipfile
├── Pipfile.lock
├── README.md