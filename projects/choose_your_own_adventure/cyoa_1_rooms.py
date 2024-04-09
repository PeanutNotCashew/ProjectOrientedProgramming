# The structure of the program is set up like a choose your own adventure book:
# 1. Display a description of the scene
# 2. Display the possible choices that can be made
# 3. Redirect to the choice selected (done by calling another function)

def shack():
    # Description of scene
    print("\nYou are in a rundown shack. There is sand tracked all over the floor. Through the singular open door, you see more sand.\n")
    # Possible choices to be made
    print("Actions:\n1. Go outside.\n")

    # Allows the user to make a choice by typing the number associated
    action = input("Type the number of your action: ")

    # After user makes choice, decide which action is carried out
    if action == "1":
        # Redirects to yard
        yard()
    elif action != "exit":
        # Error message if the input is improper
        print("That's not an action.")
        # Redoes everything in the function so that user can reinput a choice
        shack()
    # Note: if "exit" is input, nothing should occur & the program exits

def yard():
    print("\nYou're outside. All you can see is sand, sand, sand for miles. There's a shack, but not much else.\n")
    print("Actions:\n1. Go in the shack.\n")

    action = input("Type the number of your action: ")

    if action == "1":
        shack()
    elif action != "exit":
        print("That's not an action.")
        yard()

yard()