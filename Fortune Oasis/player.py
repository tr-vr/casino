# This will contain the players information
# - Username:
# - Current Wallet Amount:
# - Total Wagered:

# Will want to learn how to store this information, so that when a player 
#   finishes playing they will be able to continue where they left off from.

import sqlite3

# Create a connection to the data base
def connect():
    con = sqlite3.connect('playerinfo.db')
    cur = con.cursor()
    return con, cur

# Create playerstats database 
def create_database():
    con, cur = connect()
    cur.execute('''CREATE TABLE IF NOT EXISTS "playerstats" (
                "users" text PRIMARY KEY,
                "defaultgame" text,
                "balance" real,
                "wagered" real,
                "crackerWins" real,
                "crackerLoss" real,
                "crackerPnL" real,
                "DiceWin" real,
                "DiceLoss" real,
                "DicePnL" real,
                "TotalPnL" real)''')

# Commit the changes + terminate connection to database
def send(con):
    con.commit()
    con.close()

# Get a list of usernames