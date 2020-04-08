import sys
import time

def average_height(average_height):
    print("""Average height of the team: {} inches.
        """.format(average_height))

def player_height(player_height,item, team_height):
    player_height = (item["height"])
    player_height= player_height[:2]
    player_height = int(player_height)
    team_height.append(player_height)

def no_player():
    print("Sorry, we don't have this player in this team.")
    again_input = input("""
    Would you like to search again? [y] or [n]
    """)
    if again_input == "n":
        sys.exit("Bye Bye!")
    else:
        start()


def print_experience(team_experienced):
    print("""
    Number of experinced players:   {} 
    Number of inexperinced players: {}
    """.format(team_experienced.count(True),team_experienced.count(False)))
    


def search_again():
    print("---------------------------------------")
    again_input = input("""
    Would you like to search again? [y] or [n]
    """)
    if again_input == "n":
        sys.exit("Bye Bye!")
    else:
        start()


def player_on_team():
    print("""
    Players on team:
    """)


TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {   'name': 'Sammy Adams',
        'guardians': 'Jeff Adams and Gary Adams',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]


def start():
    for index, item in enumerate(TEAMS,1):
        print(index,") ",item)
    
    while True:
        try:    
            input_teams = int(input("""
            
            Please choose the team  >  """))
            print(""" """)
            if input_teams > 3:
                raise ValueError("""
            Invalid number. Please choose numbers from 1-3. Thanks""")
            if input_teams < 1:
                raise ValueError("""
            Invalid number. Please choose numbers from 1-3. Thanks""")
        except ValueError as error:
            if "invalid literal" in str(error):
                print("""
                Invalid input. Please try again by typing an integer number from 1-3. Thanks
            """)
            else:
                print(error)
        else:
            time.sleep(1)    
            if input_teams == 1: # --------------here starts the PANTHERS team statistics-------------------
                print("""

                Team {} Stats:
                --------------------
                Total players : {}

                """.format(TEAMS[0],len(PLAYERS[:6])))   
                panthers = []
                panthers_dict = []
                team_height = []
                team_experienced = []
                num=0
                for item in PLAYERS[:6]:
                    player_name = item["name"] 
                    player_experience = item["experience"]
                    if "YES" in player_experience:
                        player_experience = True
                    else:
                        player_experience = False
                    team_experienced.append(player_experience)
                    player_height(player_height, item, team_height)
                    player_stats= item
                    panthers.insert(num, player_name)
                    panthers_dict.insert(num, player_stats )
                    num +=1    
                panthers_inline = " , ".join(panthers) 
                time.sleep(1)
                print_experience(team_experienced)
                average_height = sum(team_height) / len(PLAYERS[:6])
                average_height = round(average_height,1)
                time.sleep(1)
                print("""Average height of the team: {} inches.
                """.format(average_height))
                time.sleep(1)
                player_on_team()
                time.sleep(1)
                print("***",panthers_inline,"***")
                input_player = input("""
Please choose a player.Type player's name :
-------------------------------\n>   """) 
                if input_player in panthers:
                    panthers1, panthers2, panthers3, panthers4, panthers5, panthers6 = panthers_dict
                    if input_player == panthers1["name"]:
                        for key, value in panthers1.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == panthers2["name"]:
                        for key, value in panthers2.items():
                            print(key.capitalize(), " : ", value) 
                    elif input_player == panthers3["name"]:
                        for key, value in panthers3.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == panthers4["name"]:
                        for key, value in panthers4.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == panthers5["name"]:
                        for key, value in panthers5.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == panthers6["name"]:
                        for key, value in panthers6.items():
                            print(key.capitalize(), " : ", value)
                    search_again()
                else:
                    no_player() 
            elif input_teams == 2: # --------------here starts the BANDITS team statistics-------------------
                time.sleep(1)
                print("""

                Team {} Stats:
                --------------------
                Total players : {}

                """.format(TEAMS[1],len(PLAYERS[6:12]))) 
                bandits = []
                bandits_dict = []
                team_height = []
                team_experienced = []
                num =0
                for item in PLAYERS[6:12]:
                    player_name = item["name"]
                    player_experience = item["experience"]
                    if "YES" in player_experience:
                        player_experience = True
                    else:
                        player_experience = False
                    team_experienced.append(player_experience)
                    player_height(player_height, item, team_height)
                    player_stats= item
                    bandits.insert(num, player_name)
                    bandits_dict.insert(num, player_stats )
                    num +=1         
                bandits_inline = " , ".join(bandits) 
                time.sleep(1)
                print_experience(team_experienced)
                average_height = sum(team_height) / len(PLAYERS[6:12])
                average_height = round(average_height,1)
                time.sleep(1)
                print("""Average height of the team: {} inches.
                """.format(average_height))
                time.sleep(1)
                player_on_team()
                time.sleep(1)
                print(bandits_inline) 
                input_player = input("""
Please choose a player.Type player's name :
-------------------------------\n>   """)
                if input_player in bandits:
                    bandits1, bandits2, bandits3, bandits4, bandits5, bandits6 = bandits_dict
                    if input_player == bandits1["name"]:
                        for key, value in bandits1.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == bandits2["name"]:
                        for key, value in bandits2.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == bandits3["name"]:
                        for key, value in bandits3.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == bandits4["name"]:
                        for key, value in bandits4.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == bandits5["name"]:
                        for key, value in bandits5.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == bandits6["name"]:
                        for key, value in bandits6.items():
                            print(key.capitalize(), " : ", value)
                    search_again()
                else:
                    no_player() 

            else:      # --------------here starts the WARRIORS team statistics-------------------
                time.sleep(1)
                print("""

                Team {} Stats:
                --------------------
                Total players : {}

                """.format(TEAMS[2],len(PLAYERS[12:])))
                warriors = []
                warriors_dict = []
                team_height = []
                team_experienced = []
                num =0
                for item in PLAYERS[12:]:
                    player_name = item["name"]
                    player_experience = item["experience"]
                    if "YES" in player_experience:
                        player_experience = True
                    else:
                        player_experience = False
                    team_experienced.append(player_experience)
                    player_height(player_height, item, team_height)
                    player_stats= item
                    warriors.insert(num, player_name)
                    warriors_dict.insert(num, player_stats )
                    num +=1     
                warriors_inline = " , ".join(warriors) 
                time.sleep(1)
                print_experience(team_experienced)
                average_height = sum(team_height) / len(PLAYERS[6:12])
                average_height = round(average_height,1)
                time.sleep(1)
                print("""Average height of the team: {} inches.
                """.format(average_height))
                time.sleep(1)
                player_on_team()
                time.sleep(1)
                print(warriors_inline) 
                input_player = input("""
Please choose a player.Type player's name :
-------------------------------\n>   """)       
                if input_player in warriors:
                    warriors1, warriors2, warriors3, warriors4, warriors5, warriors6 = warriors_dict
                    if input_player == warriors1["name"]:
                        for key, value in warriors1.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == warriors2["name"]:
                        for key, value in warriors2.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == warriors3["name"]:
                        for key, value in warriors3.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == warriors4["name"]:
                        for key, value in warriors4.items():
                            print(key.capitalize(), " : ", value) 
                    elif input_player == warriors5["name"]:
                        for key, value in warriors5.items():
                            print(key.capitalize(), " : ", value)
                    elif input_player == warriors6["name"]:
                        for key, value in warriors6.items():
                            print(key.capitalize(), " : ", value)
                    search_again()
                else:
                    no_player()
if __name__ == "__main__": 
    start()

