# INTRODUCED CONCEPTS: dictionaries
# Similar to lists, is a sequence
# Contains items as "keys" and "values," similar to words and their definitions in paper dictionaries
# Items are accessed like lists, but are indexed according to key and not location
# Thus, keys cannot repeat, since accessing a key might return multiple values
# Syntax: dictionary = {"key": "value"}

# Prompt: Given a string of roman numerals, return the decimal representation

# Creates a dictionary associating roman numerals with their decimal values
roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

userInput = "MCMXCIV" # Testing string

programOutput = 0

for i in range(len(userInput) - 1):
    currentLetter = userInput[i]
    # An error is given if trying to access a list member that does not exist.
    # Thus, 1 is subtracted from the length of the list in the range() function.
    # This means that this next line will not cause an error
    nextLetter = userInput[i + 1]

    # Filtering for exceptions: when letters must be subtracted
    if (currentLetter == "I") and ((nextLetter == "V") or (nextLetter == "X")):
        programOutput -= roman[currentLetter]
    elif (currentLetter == "X") and ((nextLetter == "L") or (nextLetter == "C")):
        programOutput -= roman[currentLetter]
    elif (currentLetter == "C") and ((nextLetter == "D") or (nextLetter == "M")):
        programOutput -= roman[currentLetter]
    # If no applicable exception...
    else:
        programOutput += roman[currentLetter]

# userInput[-1] accesses the array backwards, and returns the last value
# Since the last numeral is not added in order to prevent an error above,
# the next numeral must be added outside the loop
programOutput += roman[userInput[-1]]

print(programOutput)