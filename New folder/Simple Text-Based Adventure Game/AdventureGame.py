def start_game():
    print("Welcome to the Enchanted Forest Adventure!")
    print("In this game, you will make choices that affect your journey.")
    print("You are standing at the entrance of a dark forest.")
    first_choice()

def first_choice():
    choice = input("Do you want to enter the forest or walk around it? (enter/walk): ").strip().lower()
    if choice == "enter":
        enter_forest()
    elif choice == "walk":
        walk_around()
    else:
        print("Invalid choice. Please type 'enter' or 'walk'.")
        first_choice()

def enter_forest():
    print("You venture deep into the forest and hear a rustling noise.")
    choice = input("Do you want to investigate the noise or keep walking? (investigate/walk): ").strip().lower()
    if choice == "investigate":
        investigate_noise()
    elif choice == "walk":
        find_clearing()
    else:
        print("Invalid choice. Please type 'investigate' or 'walk'.")
        enter_forest()

def investigate_noise():
    print("You discover a small fairy trapped under a fallen branch.")
    choice = input("Do you want to help the fairy or leave her? (help/leave): ").strip().lower()
    if choice == "help":
        print("The fairy is grateful and grants you a wish!")
        wish_choice()
    elif choice == "leave":
        print("You leave the fairy and continue your journey.")
        find_clearing()
    else:
        print("Invalid choice. Please type 'help' or 'leave'.")
        investigate_noise()

def wish_choice():
    choice = input("Do you wish for (wealth) or (knowledge)? ").strip().lower()
    if choice == "wealth":
        print("You are now rich beyond your wildest dreams! Congratulations!")
    elif choice == "knowledge":
        print("You gain wisdom and insights that will guide you throughout your life!")
    else:
        print("Invalid choice. Please type 'wealth' or 'knowledge'.")
        wish_choice()
    end_game()

def walk_around():
    print("You choose to walk around the forest and discover a hidden path.")
    choice = input("Do you want to follow the path or return home? (follow/return): ").strip().lower()
    if choice == "follow":
        find_clearing()
    elif choice == "return":
        print("You safely return home, but wonder what adventures you missed.")
        end_game()
    else:
        print("Invalid choice. Please type 'follow' or 'return'.")
        walk_around()

def find_clearing():
    print("You find a beautiful clearing filled with flowers and a sparkling pond.")
    choice = input("Do you want to rest by the pond or explore further? (rest/explore): ").strip().lower()
    if choice == "rest":
        print("You take a moment to relax and enjoy the beauty around you.")
        end_game()
    elif choice == "explore":
        print("You discover a hidden treasure chest!")
        treasure_choice()
    else:
        print("Invalid choice. Please type 'rest' or 'explore'.")
        find_clearing()

def treasure_choice():
    choice = input("Do you want to open the treasure chest or leave it? (open/leave): ").strip().lower()
    if choice == "open":
        print("Inside the chest, you find gold coins and precious gems! You're rich!")
    elif choice == "leave":
        print("You decide to leave the treasure chest untouched, valuing adventure over riches.")
    else:
        print("Invalid choice. Please type 'open' or 'leave'.")
        treasure_choice()
    end_game()

def end_game():
    print("Thank you for playing! Your adventure ends here.")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("Goodbye! Until next time.")
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        play_again()

# Start the game
start_game()