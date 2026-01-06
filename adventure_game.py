# adventure_game.py
# An interactive text-based adventure game where the player searches for a legendary treasure.

import random
import time

player = {
    "name": "",
    "health": 100,
    "inventory": []
}

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def start_game():
    slow_print("\n🌟 Welcome to THE LEGEND OF THE ANCIENT TREASURE 🌟\n")
    player["name"] = input("Enter your name, explorer: ").strip()

    slow_print(f"\nGreetings, {player['name']}!")
    slow_print("Your mission is to find the legendary treasure hidden in this land.\n")

    game_loop()

def game_loop():
    while player["health"] > 0:
        slow_print("\nYou arrive at a crossroads.")
        slow_print("1. Enter the Dark Forest 🌲")
        slow_print("2. Explore the Mysterious Cave 🕳️")
        slow_print("3. Check Status 📜")

        choice = input("\nChoose an option (1/2/3): ")

        if choice == "1":
            forest_path()
        elif choice == "2":
            cave_path()
        elif choice == "3":
            show_status()
        else:
            slow_print("❌ Invalid choice.")

def show_status():
    slow_print(f"\n❤️ Health: {player['health']}")
    slow_print(f"🎒 Inventory: {player['inventory'] if player['inventory'] else 'Empty'}")

def forest_path():
    slow_print("\n🌲 You step into the dark forest...")
    event = random.choice(["river", "beast", "tree"])

    if event == "river":
        slow_print("You find a glowing river.")
        slow_print("1. Drink water")
        slow_print("2. Follow the river")

        choice = input("Choose: ")

        if choice == "1":
            slow_print("✨ The water heals you!")
            player["health"] = min(100, player["health"] + 20)
        else:
            slow_print("🏆 You discover an ancient treasure chest!")
            win_game()

    elif event == "beast":
        slow_print("🐺 A wild beast attacks you!")
        damage = random.randint(10, 30)
        player["health"] -= damage
        slow_print(f"You lose {damage} health!")

        if "sword" not in player["inventory"]:
            slow_print("You find a sword after escaping.")
            player["inventory"].append("sword")

    else:
        slow_print("🌳 You climb a tree and find a mysterious key.")
        if "key" not in player["inventory"]:
            player["inventory"].append("key")

def cave_path():
    slow_print("\n🕳️ The cave is cold and dark...")

    if "torch" not in player["inventory"]:
        slow_print("You find an unlit torch.")
        player["inventory"].append("torch")

    slow_print("1. Light the torch")
    slow_print("2. Walk in darkness")

    choice = input("Choose: ")

    if choice == "1":
        if "key" in player["inventory"]:
            slow_print("🔑 You unlock a hidden door!")
            win_game()
        else:
            slow_print("🐍 You avoid traps but find nothing.")
    else:
        slow_print("💀 You fall into a pit!")
        player["health"] = 0
        lose_game()

def win_game():
    slow_print("\n🏆 YOU FOUND THE LEGENDARY TREASURE!")
    slow_print("🎉 Congratulations, you win the game!")
    restart_game()

def lose_game():
    slow_print("\n💀 You have failed your quest.")
    restart_game()

def restart_game():
    choice = input("\nDo you want to restart the game? (yes/no): ").lower()
    if choice == "yes":
        player["health"] = 100
        player["inventory"] = []
        game_loop()
    else:
        slow_print("\n👋 Farewell, brave explorer!")
        exit()

# Start the adventure
start_game()
