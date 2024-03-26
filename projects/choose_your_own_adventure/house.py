# Creating a mini Choose Your Own Adventure

def shack():
    print("\nYou are in a rundown shack. There is sand tracked all over the floor. Through the singular open door, you see more sand.\n")
    print("Actions:\n1. Go outside.\n")

    action = input("Type the number of your action: ")

    if action == "1":
        yard()
    elif action != "exit":
        print("That's not an action.")
        shack()

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