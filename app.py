import constants
import sys


print("""
         ----------------------------
          BASKETBAL TEAM STATS TOOL
        ----------------------------
""")
print("""

---- MENU ----

""")

print("""Here are your options:

1) Display Team Stats
2) Quit
""")

first_input = int(input("""
            Enter and option >  """))
print(""" 
""")
if first_input == 2:
    sys.exit("Sorry to hear that. Bye.")
    
elif first_input == 1:
    constants.start()
