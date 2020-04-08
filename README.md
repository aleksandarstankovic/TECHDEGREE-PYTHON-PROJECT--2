# Basketball Team Stats Tool
In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.


In these project, I needed to convert , many of the databases and information inside of them, to another type of databases and another type of data.

Main focus and problem was, how should I approach and select the key:value pairs inside each dictionary, which were inside of another List? I found a solution in :

    "for item in PLAYERS[:6]:" and then assigning the key values to each item , which I asigned to newly created variables, which I the append to newly created lists:

    "player_name = item["name"] "
    "player_guardians = item["guardians"] "

From that point I built up on that. 

I had problems with understanding how and when should I use DUNDER MAIN, but I think I got it good on the project, although I feel that I can improve a lot more in that.

Also, I found a problem to distribute the players equaly to the teams based on their experiences, although I converted their experience "YES" and "NO" values to True and False. I resolved it with a little bit more advanced usage of "slices", example:
  
   sliced_joined_players = PLAYERS[:3] + PLAYERS[8:11]
   for item in sliced_joined_players:

For the very end, and for your pleasure, I added the possibility that after you type your player's name, all of his info pops up. It is just the thing that I thought was missing in this app and that we should allow the users to go deep into the player's information, and not just the team's.
