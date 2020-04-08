# Basketball Team Stats Tool
In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.


In these project, I needed to convert , many of the databases and information inside of them, to another type of databases and another type of data.

Main focus and problem was, how should I approach and select the key:value pairs inside each dictionary, which were inside of another List? I found a solution in :

    "for item in PLAYERS[:6]:" and then assigning the key values to each item , which I asigned to newly created variables, which I the append to newly created lists:

    "player_name = item["name"] "
    "player_guardians = item["guardians"] "

From that point I built up on that. 

Knowing that it was not part of the task, anyway I added the posibility to type the name of the each player, and information from that player will pop up. I felt that without that part this project and application is not complete.

I had problems with understanding how and when should I use DUNDER MAIN, but I think I got it good on the project, although I feel that I can improve a lot more in that.

Also, I found a problem to distribute the players equaly to the teams based on their experiences, although I converted their experience "YES" and "NO" values to True and False.

