print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# takes player input on which way to go.
cross_road = input("You're at a cross road."
                   " where do you want to go?\nType 'left' or 'right': ").lower()
if cross_road == "left":
    #takes player input to wait or swim
    sea = input("Great choice.....You've come to a sea."
          " there's an island in the middle of the sea\n"
                "Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if sea == "wait":
    # takes player inpur on which door they choose
        door = input("You arrived at the island unharmed,"
                     "there is a house with 3 doors;"
                     " red, yellow and blue. which do you choose? ").lower()
        if door == "red":
            print("It's a room full of deadly snakes.GAME OVER")
        elif door == "yellow":
            print("You did it! You found the treasure")
        elif door == "blue":
            print("You entered thee home of an angry giant. GAME OVER")

        else:
            print("You are trapped.GAME OVER")
    else:
        print("You got attacked by sharks")

else:
    print("you fell into a whole.....GAME OVER")