""" Main class that will be used to operate the casino """
import time
import sys

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

def main():
    welcome()

if __name__ == "__main__":
    main()