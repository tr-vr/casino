""" Main class that will be used to operate the casino """
import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome(): #Introduction to the games available
    print("Welcome to Fortune Oasis")
    time.sleep(3)
    print("At Fortune Oasis, we currently have two games available.")
    time.sleep(1)
    print("Christmas Cracker [1.95x] & Dicing [2x]")
    time.sleep(2)
    print("If you want to learn how to play, type \'!rules\' in the chat below.")
    time.sleep(1)
    print("~" * 65)
    time.sleep(2)
    print("Select your game options with these commands.")
    print("Christmas Crackers: !You / !Me - OR - Dicing: !H / !L")
    

def rules():
    print("Rules at Fortune Oasis!")
    print("Christmas Crackers: To win this you must choose who will receive the Party Hat" 
          + "[50/50].")
    print("Type !You [Host] or !Me [Player].")
    print("If chosen correctly you will receive 2x")
    time.sleep(1.5)
    print("")

def main():
    welcome()
    rules()

if __name__ == "__main__":
    main()