import random
random.seed(1234)

print("Program starting.")
print("Welcome to the rock-paper-scissors game!")
player_name = input("Insert player name: ")
print(f"Welcome {player_name}!")
print("Your opponent is RPS-3PO.")
print("Game starts...\n")

choices = {1: "rock", 2: "paper", 3: "scissors"}
results = {"player_wins": 0, "bot_wins": 0, "draws": 0}

while True:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    try:
        player_input = int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 0 to 3.\n")
        continue

    if player_input == 0:
        break
    if player_input not in [1, 2, 3]:
        print("Invalid choice. Please choose 1, 2, 3 or 0.\n")
        continue

    bot_input = random.randint(1, 3)

    print("Rock! Paper! Scissors! Shoot!\n")
    print("#" * 25)
    print(f"{player_name} chose {choices[player_input]}.")
    print("#" * 25)
    print(f"RPS-3PO chose {choices[bot_input]}.")
    print("#" * 25)
    print()

    if player_input == bot_input:
        print(f"Draw! Both players chose {choices[player_input]}.\n")
        results["draws"] += 1
    elif (player_input == 1 and bot_input == 3) or \
         (player_input == 2 and bot_input == 1) or \
         (player_input == 3 and bot_input == 2):
        print(f"{player_name} {choices[player_input]} beats RPS-3PO {choices[bot_input]}.\n")
        results["player_wins"] += 1
    else:
        print(f"RPS-3PO {choices[bot_input]} beats {player_name} {choices[player_input]}.\n")
        results["bot_wins"] += 1

print("Results:")
print(f"{player_name} - wins ({results['player_wins']}), losses ({results['bot_wins']}), draws ({results['draws']})")
print(f"RPS-3PO - wins ({results['bot_wins']}), losses ({results['player_wins']}), draws ({results['draws']})")
print("\nProgram ending.")
