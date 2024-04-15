# INTRODUCED CONCEPTS: classes

class Pet:
    # Called a "constructor". The class points to this function in order to set values for a created object.
    def __init__(self, animalType, name, diet):
        self.typeOfAnimal = animalType
        self.name = name
        self.diet = diet
        self.timesFedToday = 0

    # A method within the class. All objects of this class have this same method.
    def feed(self):
        # Choose from list of edible options
        # Print out all options
        for food in self.diet:
            print(food)
        
        # Take in input
        foodSelected = input("Choose a food item: ")

        # Check if the selected food is in the pet's diet.
        if foodSelected.title() in self.diet:
            self.timesFedToday += 1
        else:
            print(self.name + " can't eat " + foodSelected + "!")

# Testing the class out
# Creates a pet.
# The variable name is princess
# Uses the __init__ function to assign values inside the object
princess = Pet("Dog", "Princess", ("Kibble", "Dog treat", "Human food"))
princess.feed()
# Variables inside an instance of a class can also be accessed from outside
print("Princess was fed " + str(princess.timesFedToday) + " time today.")

# Creates another pet object. To demonstrate reusability.
slithers = Pet("Snake", "Slithers", ("Mice", "Pinkie"))
slithers.feed()
