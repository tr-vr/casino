""" This will contain the players information
Username:
Current Wallet Amount:
Total Wagered:

Will want to learn how to store this information, so that when a player quits how they will
resume the game will the stats from last time. 
"""

import sqlite3

con = sqlite3.connect('playerinfo.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS playerstats
                (user text, defaultgame text, balance real, wagered real, 
                crackerWins real, crackerLoss real, crackerPnL real,
                DiceWin real, DiceLoss real, DicePnL real, TotalPnL real)''')