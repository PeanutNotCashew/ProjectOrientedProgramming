# Importing a json package allows us to understand the file containing room information
import json

# Opens the file containing json. This indicates that we want to read the file, and that the format of the file is text.
with open("rooms.json", "rt") as f:
    fileAsString = f.read()
# This parses the text in the json file and creates a dictionary containing the information needed for the program.
rooms = json.loads(fileAsString)

inventory = []
programInProgress = True # Used for exiting the program
room = rooms["yard"] # Set starting room

def checkInventory():
    if len(inventory) > 0:
        print("\nItems currently in your inventory:")
        for i in inventory:
            print(i)
    else:
        print("\nYou do not have anything in your inventory.")

# Checks if "action" is a number within the inclusive range [1, numOfActions]
def validActionNum(action, numOfActions):
    if action.isdigit():
        if (int(action) >= 1) and (int(action) <= numOfActions):
            return True
    return False

# Note: this program uses a loop rather than recursion and method redirects since rooms are handled in an external file rather than in individual methods. This also reduces memory usage.
while programInProgress:
    print("\n---------------------") # A divider, for aesthetics
    # Prints room description
    print(room["description"])

    # Prints room actions
    numOfActions = len(room["actions"])
    print("\nActions:")
    for i in range(numOfActions):
        # Prints action number and action description
        actionDescription = room["actions"][i]["description"]
        print(str(i+1) + ". " + actionDescription)
    print("i. Access inventory")

    # Gets input
    action = input("Type the number of your action: ")

    # Carries out actions
    if action == "exit":
        programInProgress = False # Ends loop
    elif action == "i":
        checkInventory()
    elif validActionNum(action, numOfActions):
        actionNum = int(action) - 1
        # If any item should be added to inventory, add it
        for i in room["actions"][actionNum]["inventory"]:
            inventory.append(i)
        # Go to next room
        nextRoom = room["actions"][actionNum]["redirect"]
        room = rooms[nextRoom]
    else:
        print("That's not an action.")