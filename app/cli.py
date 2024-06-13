# app/cli.py

from app.helpers import (
    init_database,
    create_team,
    create_player,
    create_match,
    create_coach,  # Add the import for create_coach
    list_teams,
    list_coaches,
    list_players,
    find_team_by_name,  # Add the imports for find functions
    find_player_by_name,
    find_coach_by_name,
    exit_program
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            name = input("Enter team name: ")
            city = input("Enter city: ")
            coach_name = input("Enter coach name: ")
            create_team(name, city, coach_name)
        elif choice == "2":
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team_id = int(input("Enter team ID: "))
            create_player(name, position, team_id)
        elif choice == "3":
            date = input("Enter match date (YYYY-MM-DD): ")
            location = input("Enter match location: ")
            home_team_id = int(input("Enter home team ID: "))
            away_team_id = int(input("Enter away team ID: "))
            create_match(date, location, home_team_id, away_team_id)
        elif choice == "4":
            list_teams()
        elif choice == "5":
            list_coaches()
        elif choice == "6":
            list_players()
        elif choice == "7":
            name = input("Enter team name: ")
            find_team_by_name(name)
        elif choice == "8":
            name = input("Enter player name: ")
            find_player_by_name(name)
        elif choice == "9":
            name = input("Enter coach name: ")
            find_coach_by_name(name)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a team")
    print("2. Create a player")
    print("3. Create a match")
    print("4. List all teams")
    print("5. List all coaches")
    print("6. List all players")
    print("7. Find team by name")
    print("8. Find player by name")
    print("9. Find coach by name")

if __name__ == "__main__":
    main()
