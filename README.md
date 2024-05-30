Fortune Oasis Casino

Developing an terminal based game currently with two game mode: Christmas Crackers and Dicing.

Want to learn how to store player data locally, to keep track of their total wagered + winning records + current balance which should be all connected to their player ID

To do list:
- implement the select func (user can select from the menu what options to do)
- implement christmas crackers
    - dialogue
    - fair randomisation

- implement player
- implement player sqlite to hold id, information, stats
    - decide whether to use a csv file or sqlite database

UPDATE 30th May 2024
I have now decided to use a database to store player information linked to their
playerid.

This will include their player balance, logs, total wagered, etc...

- Perhaps may require a password aswell and a login / register menu now which 
will be required before you log into the game menu.

TO DO:
Player - build up database to store information

MAIN - Rearrange main menu to have the login prior to display the welcome 
messages