""" Main class that will be used to operate the casino """
import time
import christmas_crackers, higher_lower, player

def setmode(x = christmas_crackers):
    return x.name()

def welcome(): 
    """ Welcome message when the program is ran """
    print("Welcome to Fortune Oasis!")
    print('.' * 25)
    time.sleep(3)
    print("At Fortune Oasis, we currently have two games available.")
    time.sleep(1)
    print("Christmas Cracker [1.95x] & Dicing [2.0x].")
    time.sleep(2)
    print("If you want to learn how to play, type \'!rules\' in the chat below.")
    time.sleep(1)
    print("~" * 66)
    time.sleep(2)
    print("Select your game options with these commands.")
    print("Begin by typing !Trade to enter into a offer.")
    print("Christmas Crackers: !You / !Me - OR - Dicing: !H / !L")
    
def rules():
    """ Basic rules on on how to play. """
    print('-' * 23)
    print("Rules at Fortune Oasis!")
    print('-' * 23)
    print()
    time.sleep(1.5)
    print("Christmas Crackers: A Christmas cracker is pulled & either the Host "
          + "or Player will receive a prize [50/50].")
    print("Type !You [Host] or !Me [Player]. Pick correctly to win [1.95x].")
    print()
    print("Dicing: A fair 0 - 100 sided dice is rolled.")
    print("Type !H [55-100] or !L [0 - 50]. Pick correctly to win [2.0x].")
    print()
    print("To begin type !Trade or change your game mode with !You !Me !H !L")

def userinput(): 
    """
    Case-insensitive user input
    """
    return input(">>> ").casefold()

def trade():
    print("Sending trade request...")
    return input("Offer? ")

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
        print("You have offered " + i + " Oasis Points on " + setmode())
    elif x == 'exit':
        print("\033[31m" + "Thank you for playing! We hope to see you next time.")
        exit()
    else:
        print("*** You have entered in an invalid command ***")
        print("[Type '!help' to see all available options].")
    
if __name__ == "__main__":
    welcome()
    while True:
        menu(userinput())