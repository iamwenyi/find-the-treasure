print("Welcome to Find The Treasure! Type an answer to find out what will happen next. Try to find the treasure, good luck!")
print("--------------------------------------------")

print("You wake up on a deserted island. There are two ways you can go to: right or left. Enter which way you want to go to.")
print("")
direction_choice = input("Enter here: ")

if direction_choice == "right":
    print("")
    print("You fall into a deep hole full of butts. They fart at you and you die of suffocation. Game over!")
elif direction_choice == "left":
    print("")
    print("You reach a big ocean. You can either wait for a boat to arrive or swim across. Enter 'wait' if you want to wait for a boat, or 'swim' if you want to swim across.")
    print("")
    ocean_choice = input("Enter here: ")
    if ocean_choice == "wait":
        print("")
        print("The boat came and dropped you off at a big temple with 4 doors coloured red, blue, yellow, and green. Type in the coloured door you want to go to.")
        colour_choice = input("Enter here: ")
        if colour_choice == "red":
            print("")
            print("As you walk in the room, you find a fat, naked lady wanting to kiss you. You die of shock. Game over!")
        elif colour_choice == "blue":
            print("")
            print("As you step in, a scorpion suddenly comes and poisons you. Game over!")
        elif colour_choice == "yellow":
            print("")
            print("You find a glowing light in front of you. You walk up to it, and you realize you found the treasure! You win!")
        elif colour_choice == "green":
            print("")
            print("Once you step in, a crazy man suddenly comes and stabs you with a knife. You die of losing too much blood. Game over!")
        else:
            print("")
            print("You got struck by lightning as you disobeyed the person who coded this. Game over!")
    elif ocean_choice == "swim":
        print("")
        print("A water ghost grabs you by your leg and pulls you underwater. You drown. Game over!")
    else:
        print("")
        print("You got struck by lightning as you disobeyed the person who coded this. Game over!")
else:
    print("")
    print("You got struck by lightning as you disobeyed the person who coded this. Game over!")
