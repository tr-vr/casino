""" Main class that will be used to operate the casino """
import time

def welcome(): #Introduction to the games available
    print("Welcome to Fortune Oasis")
    time.sleep(3)
    print("At Fortune Oasis, we currently have Christmas Crackers & Dicing available.")
    time.sleep(3)
    print("If you want to learn how to play, type \'!rules\' in the chat below.")
    time.sleep(3)
    print()
    print("Select your game options with these commands.")
    print("Christmas Crackers: !You / !Me - OR - Dicing: !H / !L")

def rules():
    

def main():
    welcome()

if __name__ == "__main__":
    main()