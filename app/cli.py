# app/cli.py

from app.helpers import (
    create_team,
    create_player,
    list_teams,
    list_players,
    find_team_by_name,
    find_player_by_name,
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
            create_team(name, city)
        elif choice == "2":
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team_id = int(input("Enter team ID: "))
            create_player(name, position, team_id)
        elif choice == "3":
            list_teams()
        elif choice == "4":
            list_players()
        elif choice == "5":
            name = input("Enter team name: ")
            find_team_by_name(name)
        elif choice == "6":
            name = input("Enter player name: ")
            find_player_by_name(name)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a team")
    print("2. Create a player")
    print("3. List all teams")
    print("4. List all players")
    print("5. Find team by name")
    print("6. Find player by name")

if __name__ == "__main__":
    main()
