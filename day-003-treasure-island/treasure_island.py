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
print("You proceed into the search area and find a split path ahead.")
# Pathways of nested ifs
choice1 = input("You\'re at a crossroad, where do you want to go? "
                "Type 'left' or 'right': ").lower()
if choice1 == "left":
    # continue the game
    print("You have arrived at a river. There is a sign that mentions a nearby castle toward the end of the river.")
    choice2 = input("Decide if you want to wait for the next boat or swim to the castle."
                    "\nType 'wait' or 'swim': ").lower()
    if choice2 == "wait":
        # continue to final game stage
        choice3 = input("You have arrived safely at the castle after an 90-minute boat ride.\nYou proceed to enter"
                        " through the large doors into a mysteriously beautiful foyer.\nYou begin your search down the"
                        " corridor ahead.\nThere are several doors to choose from. \nMost doors are black metal."
                        " But you notice 3 doors; each door in a different color.\nSelect which door you want to enter."
                        "\nType 'red', 'yellow' or 'blue': ").lower()
        if choice3 == "red":
            print("Oh no, you have found yourself in a room full of cloaked creatures."
                  "\nThey have captured you and burned you by fire. Game Over!")
        elif choice3 == "yellow":
            print("Before your eyes, you see a throne with a large chest.\nYou take the key from the nearby table"
                  " and unlock the chest.\nYes, you have found the treasure. You win!")
        elif choice3 == "blue":
            print("You proceed to explore the room. But behind you, you hear a growl."
                  "\nHiding in the shadows are 2 strange beasts. They decide to make you their dinner. Game Over!")
        else:
            print("Sorry you've chosen a non-existent door. Game over!")
    else:
        print("You got attacked by a large swarm of mutated trout. Game Over!")
else:
    print("You have traveled into a dark area. While running you fall into a hole. Sorry, Game Over!")
