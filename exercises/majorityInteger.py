# INTRODUCED CONCEPTS: tuples and lists
# Both tuples and lists are lists of data which can contain any combination of data types (integers, floats, strings, booleans, etc.)
# Tuples are "immutable", or unchangeable. After creating them, items cannot be altered, changed, or removed
# Lists are "mutable", and can be altered after creation.

# Prompt: Given a list of integers, return the majority element. It there is no majority element, return if the array is majority even or odd numbers; and if there is none, say so.

import random

def majority(numberList):
    # Tallying up the frequencies of each number
    values = []
    frequencies = []

    for i in numberList:
        # If an item is already in the list, increase the tally by one
        if i in values:
            itemLocation = values.index(i) # Finds the location of the item in the tallies
            frequencies[itemLocation] += 1

        # If an item is not in the list, add it to the list and increase the tally by one
        else:
            values.append(i)
            frequencies.append(1)

    # Checking for the common integer
    highestFrequency = 0
    duplicate = False

    for i in frequencies:
        # If the highest frequency so far, update variable storing highest frequency
        if i > highestFrequency:
            highestFrequency = i
            duplicate = False

        # If 2 integers have the same frequency, there is no majority
        elif i == highestFrequency:
            duplicate = True

    if duplicate == False: # Check that there isn't a tie before declaring a majority
        majorityInt = values[frequencies.index(highestFrequency)]
        return str(majorityInt)

    # Checking whether evens/odds are more common
    evens = 0
    odds = 0
    for i in range(len(values)):
        # If value divided by 2 has a remainder of zero. AKA, if even.
        # This operator is called modulo
        if values[i] % 2 == 0:
            evens += frequencies[i]
        else:
            odds += frequencies[i]
        i += 1

    if evens > odds:
        return "Majority evens"
    elif odds < evens:
        return "Majority odds"
    else:
        return "No majority"

# Random generation of a list of 20 integers for testing
# Each item is between 0 and 9, inclusive
inputList = []

for i in range(20):
    inputList.append(random.randint(0, 9))
    i += 1

# Print the random generated list to check against program
print(inputList)
# Print the outcome
# The function defined above is called in the following line
print(majority(inputList))