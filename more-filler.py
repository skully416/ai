import random

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def intro():
    print_slow("Welcome to the mysterious land of AdventureQuest!")
    print_slow("You find yourself in a dark forest, and you have no memory of how you got here.")
    print_slow("Your goal is to find your way back home and discover the secrets of this land.")
    print_slow("Good luck on your adventure!\n")

def choose_path():
    print_slow("You come across a fork in the road. Do you go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    while choice not in ['left', 'right']:
        choice = input("Invalid input. Please enter 'left' or 'right': ").lower()
    return choice

def explore_forest():
    print_slow("You venture deeper into the forest and encounter a wild beast!")
    print_slow("Choose your action: ")
    print_slow("1. Fight")
    print_slow("2. Run")
    choice = input("Enter '1' to fight or '2' to run: ")
    if choice == '1':
        if random.random() < 0.5:
            print_slow("You fought valiantly and defeated the beast!")
        else:
            print_slow("The beast was too strong for you. You barely managed to escape with your life.")
    else:
        print_slow("You chose to run and managed to escape the beast's grasp.")

def find_hidden_treasure():
    print_slow("You stumble upon a hidden treasure chest! It's locked.")
    print_slow("You can try to open it or continue your journey.")
    choice = input("Enter 'open' to try and open the chest or 'continue' to move on: ").lower()
    if choice == 'open':
        if random.random() < 0.3:
            print_slow("Congratulations! You managed to unlock the chest and found valuable treasures.")
        else:
            print_slow("The chest was trapped! You triggered a trap and got hurt.")
    else:
        print_slow("You decide to leave the chest and continue your journey.")

def main():
    intro()

    while True:
        path = choose_path()
        if path == 'left':
            explore_forest()
        else:
            find_hidden_treasure()

        print_slow("Do you want to continue your adventure? (yes/no)")
        choice = input("Enter 'yes' to continue or 'no' to quit: ").lower()
        if choice == 'no':
            print_slow("Thank you for playing AdventureQuest! See you next time.")
            break

if __name__ == "__main__":
    import time
    main()
