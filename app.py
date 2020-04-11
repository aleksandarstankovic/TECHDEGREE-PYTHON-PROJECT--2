import constants
import time
import sys
import random

def prints(players_experiences, average_height, join_names, join_guardians):
    print("""\nNumber of experinced players:   {} 
            \nNumber of inexperinced players: {}
            """.format(players_experiences.count(True),players_experiences.count(False)))  
    print("\nAverage team height: ",average_height, "inches\n")            
    print("\nPlayer names: \n", "\n*** ",join_names)
    print("\nPlayer's guardians: \n", "\n*** ",join_guardians)

 
print("""
        ----------------------------
        BASKETBAL TEAM STATS TOOL
        ----------------------------
""")
print("""
---- MENU ----
""")

    
def start():
    game_running1 = True
    while game_running1:
        print("""Here are your options:
            \n1) Display Team Stats
            \n2) Quit
            """)
        try:
            first_input = int(input("""
                        \nEnter and option >  """))
            if first_input > 2:
                raise ValueError("""
            Invalid number. Please choose numbers from 1-3. Thanks""")
            if first_input < 1:
                raise ValueError("""
            Invalid number. Please choose numbers from 1-3. Thanks""")
        except ValueError as error:
                if "invalid literal" in str(error):
                    print("""
                    Invalid data input! Please try again by typing an INTEGER number. Thanks
                """)
                else:
                    print(error)
        else:
            print(""" 
            """)
            if first_input == 2:
                print("Sorry to hear that. Bye.")
                game_running1 = False
                
            elif first_input == 1:
                game_running = True
                while game_running:
                    for index, item in enumerate(constants.TEAMS,1):
                        print(index,") ",item)

                    try:    
                        input_teams = int(input("""
                        
                        \nPlease choose the team  >  """))
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
                            Invalid data input! Please try again by typing an INTEGER number. Thanks
                        """)
                        else:
                            print(error)
                    else:
                        if input_teams == 1: # --------------here starts the PANTHERS team statistics-------------------
                            sliced_and_joined_players = constants.PLAYERS[:3] + constants.PLAYERS[9:12]
                            print("""
                            \nTeam {} Stats:
                            \n--------------------
                            \n\nTotal players : {}
                            """.format(constants.TEAMS[0],len(sliced_and_joined_players)))
                            sliced_joined = constants.PLAYERS[:3] + constants.PLAYERS[9:12]
                            time.sleep(1)
                            players_names = []
                            players_guardians = []
                            players_experiences = []
                            players_height = []
                            for item in sliced_joined:
                                #------------PLAYERS NAMES BLOCK-------------
                                player_names = item["name"]
                                players_names.append(player_names)
                                join_names = " , ".join(players_names)
                                #------------PLAYERS GUARDIANS BLOCK-------------
                                player_guardians = item["guardians"].split("and")
                                players_guardians.extend(player_guardians)
                                join_guardians = " , ".join(players_guardians)
                                #------------PLAYERS EXPERIENCE BLOCK-------------
                                player_experience = item["experience"]
                                if "YES" in player_experience:
                                    player_experience = True
                                else:
                                    player_experience = False
                                players_experiences.append(player_experience) 
                                    #------------PLAYERS HEIGHT BLOCK-------------
                                player_height = item["height"]
                                player_height= player_height[:2]
                                player_height = int(player_height)
                                players_height.append(player_height)
                                average_height = round(sum(players_height) / len(players_height),1)
                                #-------------PRINT AREA----------------------
                            prints(players_experiences, average_height, join_names, join_guardians)
                            input_player_name = input("\nDo you want to search the teams again? Type [y] or [n] \n")
                            if input_player_name == "y":
                                continue
                            elif input_player_name == "n":
                                print("Thanks for visiting us. Goodbye.")
                                game_running = False
                                game_running1 = False

                        # --------------here starts the BANDITS team statistics-------------------
                        elif input_teams == 2: 
                            time.sleep(1)
                            print("""
                            \nTeam {} Stats:
                            \n--------------------
                            \n\nTotal players : {}
                            """.format(constants.TEAMS[1],len(constants.PLAYERS[3:9])))
                            time.sleep(1)
                            players_names = []
                            players_guardians = []
                            players_experiences = []
                            players_height = []
                            for item in constants.PLAYERS[3:9]:
                            #------------PLAYERS NAMES BLOCK-------------
                                player_names = item["name"]
                                players_names.append(player_names)
                                join_names = " , ".join(players_names)
                                #------------PLAYERS GUARDIANS BLOCK-------------
                                player_guardians = item["guardians"].split("and")
                                players_guardians.extend(player_guardians)
                                join_guardians = " , ".join(players_guardians)
                                #------------PLAYERS EXPERIENCE BLOCK-------------
                                player_experience = item["experience"]
                                if "YES" in player_experience:
                                    player_experience = True
                                else:
                                    player_experience = False
                                players_experiences.append(player_experience) 
                                    #------------PLAYERS HEIGHT BLOCK-------------
                                player_height = item["height"]
                                player_height= player_height[:2]
                                player_height = int(player_height)
                                players_height.append(player_height)
                                average_height = round(sum(players_height) / len(players_height),1)
                                    #-------------PRINT AREA----------------------
                            prints(players_experiences, average_height, join_names, join_guardians)
                            input_player_name = input("\nDo you want to search the teams again? Type [y] or [n] \n")
                            if input_player_name == "y":
                                continue
                            elif input_player_name == "n":
                                print("Thanks for visiting us. Goodbye.")
                                game_running = False
                                game_running1 = False

                        else:
                            # --------------here starts the PANTHERS team statistics-------------------
                            print("""
                            \nTeam {} Stats:
                            \n--------------------
                            \n\nTotal players : {}
                            """.format(constants.TEAMS[2],len(constants.PLAYERS[12:])))
                            time.sleep(1)
                            players_names = []
                            players_guardians = []
                            players_experiences = []
                            players_height = []
                            for item in constants.PLAYERS[12:]:
                                #------------PLAYERS NAMES BLOCK-------------
                                player_names = item["name"]
                                players_names.append(player_names)
                                join_names = " , ".join(players_names)
                                #------------PLAYERS GUARDIANS BLOCK-------------
                                player_guardians = item["guardians"].split("and")
                                players_guardians.extend(player_guardians)
                                join_guardians = " , ".join(players_guardians)
                                #------------PLAYERS EXPERIENCE BLOCK-------------
                                player_experience = item["experience"]
                                if "YES" in player_experience:
                                    player_experience = True
                                else:
                                    player_experience = False
                                players_experiences.append(player_experience) 
                                    #------------PLAYERS HEIGHT BLOCK-------------
                                player_height = item["height"]
                                player_height= player_height[:2]
                                player_height = int(player_height)
                                players_height.append(player_height)
                                average_height = round(sum(players_height) / len(players_height),1)
                                #-------------PRINT AREA----------------------
                            prints(players_experiences, average_height, join_names, join_guardians)
                            input_player_name = input("\nDo you want to search the teams again? Type [y] or [n] \n")
                            if input_player_name == "y":
                                continue
                            elif input_player_name == "n":
                                print("Thanks for visiting us. Goodbye.")
                                game_running = False
                                game_running1 = False
if __name__ == "__main__":
    start()