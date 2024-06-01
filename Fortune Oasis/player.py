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
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "creds" (
                "username" TEXT NOT NULL,
                "master_password" BLOB NOT NULL,
                "key" BLOB NOT NULL
                );
            ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS "playerstats" (
                "username" text PRIMARY KEY,
                "defaultgame" text,
                "balance" real,
                "wagered" real,
                "crackerWins" real,
                "crackerLoss" real,
                "crackerPnL" real,
                "DiceWin" real,
                "DiceLoss" real,
                "DicePnL" real,
                "TotalPnL" real)
                ''')

# Commit the changes + terminate connection to database
def finish(con):
    con.commit()
    con.close()

# Get a list of usernames
def get_users_list():
    con, cur = connect()

    cur.execute('SELECT users FROM playerstats')
    users_list = cur.fetchall() # Fetch all information from 'users'

    finish(con)

    return users_list

def add_user(username, master_hashed, key):
    con, cur = connect()
    cur.execute()