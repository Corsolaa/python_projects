from random import randint

# The items for the game
items = ["rock", "paper", "scissors"]
# Set random item out of list
choiceComputer = items[randint(0, 2)]

# You can play it infinite :)
while True:
    player = input("Rock, Paper or Scissors? ").lower()
    match player:
        case "rock":
            match choiceComputer:
                case "paper":
                    print("Rock gets covers by paper, you lose...")
                case "scissors":
                    print("Rock crushes scissors, you WIN")
                case "rock":
                    print("That's a TIE")
        case "paper":
            match choiceComputer:
                case "rock":
                    print("Paper covers rock, you WIN")
                case "scissors":
                    print("Paper gets cut by scissors, you lose...")
                case "paper":
                    print("That's a TIE")
        case "scissors":
            match choiceComputer:
                case "paper":
                    print("Scissors cut paper, you WIN")
                case "rock":
                    print("scissors get crushed by rock, you lose...")
                case "scissors":
                    print("That's a TIE")
        case _:
            print("I think you didn't spell that correctly?")
    # Set a random item again
    choiceComputer = items[randint(0, 2)]
    print()
