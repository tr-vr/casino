""" Main class that will be used to operate the casino """
import time
import sys

def welcome(): #Introduction to the games available
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
    print("Christmas Crackers: !You / !Me - OR - Dicing: !H / !L")
    
def rules():
    print('-' * 23)
    print("Rules at Fortune Oasis!")
    print('-' * 23)
    print("Christmas Crackers: A Christmas cracker is pulled & either the Host or Player will "
          + "receive a prize [50/50].")
    print("Type !You [Host] or !Me [Player]. Pick correctly to win [1.95x].")
    time.sleep(1.5)
    print()
    print("Dicing: A fair 0 - 100 sided dice is rolled.")
    print("Type !H [55-100] or !L [0 - 50]. Pick correctly to win [2.0x].")

def userinput():
    return input(">>>")

if __name__ == "__main__":
    welcome()
    userinput()