# Main class that will be used to run the game
import time
import christmas_crackers, higher_lower, player

# For now it sets the default game mode to crackers
def setmode(x = christmas_crackers):
    return x.name()

# Welcome message when the program is ran
def welcome(): 
    print("Welcome to Fortune Oasis!")
    print('.' * 25)
    time.sleep(3)
    print("At Fortune Oasis, we currently have two games available.")
    time.sleep(1)
    print("Christmas Cracker [1.95x] & Dicing [2.0x].")
    time.sleep(2)
    print("If you want to learn how to play, type \033[31m\'!Rules\'\033"
          + "[0m in the chat below.")
    time.sleep(1)
    print("~" * 66)
    time.sleep(2)
    print("Select your game options with these commands.")
    print("Begin by typing \033[31m!Trade\033[0m to enter into a offer.")
    print("\033[31mChristmas Crackers: !You / !Me - OR - Dicing: !H / !L" 
          + "\033[0m")

# Displays the rules of each gamemode    
def rules():
    print('-' * 23)
    print("\033[1;34mRules at Fortune Oasis!\033[0m")
    print('-' * 23)
    print()
    time.sleep(1.5)
    print("Christmas Crackers: A Christmas cracker is pulled & either the Host"
          + " or Player will receive a prize [50/50].")
    print("Type !You [Host] or !Me [Player]. Pick correctly to win [1.95x].")
    print()
    print("Dicing: A fair 0 - 100 sided dice is rolled.")
    print("Type !H [55-100] or !L [0 - 50]. Pick correctly to win [2.0x].")
    print()
    print("To begin type \033[31m!Trade\033[0m or change your game mode with "
          + "!You !Me !H !L")

# Captures user input
def userinput(): 
    """
    Case-insensitive user input
    """
    return input(">>> ").casefold()

# Returns amount that Player offers. Should be integer
def trade():
    print("Sending trade request...")
    return input("Offer? ")

# This is the menu function which will output based on diff choices typed
def menu(x):
    """
    Menu options:
    - rules
    - trade
    - exit
    """
    if x == '!rules':
        return rules()
    if x == '!trade':
        i = trade()
        print()
        print("You have offered \033[1;34m" + i + "\033[0m Oasis Points on "
              + "\033[31m" + setmode() + "\033[0m")
    elif x == 'exit':
        print("\033[31m" + "Thank you for playing! We hope to see you next "
              + "time.\033[0m")
        exit()
    else:
        print("\033[1;31m" + "*** You have entered in an invalid command ***"
              + "\033[0m")
        print("[Type \033[31m'!help'\033[0m to see all available options].")
    
if __name__ == "__main__":
    welcome()
    while True:
        menu(userinput())