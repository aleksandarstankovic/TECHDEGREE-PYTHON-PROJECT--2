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
while True:
    try:
        first_input = int(input("""
                    Enter and option >  """))
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
            sys.exit("Sorry to hear that. Bye.")
            
        elif first_input == 1:
            constants.start()
