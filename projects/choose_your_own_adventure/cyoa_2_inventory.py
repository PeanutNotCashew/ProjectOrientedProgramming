# Creating a variable to store items in
inventory = []

# Creating a method/function to display the inventory
# This is contained within a function to allow reuse
def checkInventory():
    # If there is more than 0 items in the inventory...
    if len(inventory) > 0:
        print("\nItems currently in your inventory:")
        for i in inventory:
            print(i)
    # If there not more than 0 items...
    else:
        print("\nYou do not have anything in your inventory.")


# Rooms
def shack():
    print("\nYou are in a rundown shack. There is sand tracked all over the floor. Through the singular open door, you see more sand.\n")
    print("Actions:\n1. Go outside.\ni. Access inventory\n")

    action = input("Type the number of your action: ")

    if action == "1":
        yard()
    elif action == "i":
        checkInventory()
        shack()
    elif action != "exit":
        print("That's not an action.")
        shack()

def yard():
    print("\nYou're outside. All you can see is sand, sand, sand for miles. There's a shack, but not much else.\n")
    print("Actions:\n1. Go in the shack.\n2. Pick up sand.\ni. Access inventory\n")

    action = input("Type the number of your action: ")

    if action == "1":
        shack()
    elif action == "2":
        inventory.append("Sand")
        yard()
    elif action == "i":
        checkInventory()
        yard()
    elif action != "exit":
        print("That's not an action.")
        yard()

yard()