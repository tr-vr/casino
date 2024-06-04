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
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT 
                "username" TEXT NOT NULL,
                "master_hashed" BLOB NOT NULL,
                "key" BLOB NOT NULL
                );
            ''')
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "playerstats" (
                "username" BLOB NOT NULL,
                "defaultgame" TEXT,
                "balance" REAL,
                "wagered" REAL,
                "crackerWins" REAL,
                "crackerLoss" REAL,
                "crackerPnL" REAL,
                "DiceWin" REAL,
                "DiceLoss" REAL,
                "DicePnL" REAL,
                "TotalPnL" REAL,
                CONSTRAINT FK_username
                FOREIGN KEY ("username")
                REFERENCES creds(username)
                );
            ''')

# Commit the changes + terminate connection to database
def finish(con):
    con.commit()
    con.close()

# Get a list of usernames
def get_users_list():
    con, cur = connect()

    cur.execute('SELECT username FROM creds')
    users_list = cur.fetchall() # Fetch all information from 'users'

    finish(con)

    return users_list

# SQL query to add new user into the Creds table
def add_user(username, master_hashed, key):
    """
    Parameters:
    username: username chosen by user in string form
    master_hashed: hash of the password for the new user
    key: a key to encrypt and decrypt passwords
    """
    con, cur = connect()
    cur.execute(f'''
                INSERT INTO creds 
                ("username", "master_hashed", "key")
                VALUES ("{username}", "{master_hashed}", "{key}")
                ''')
    finish(con)

# SQL Query to retrieve hashed password of a selected user
def get_hash(username):
