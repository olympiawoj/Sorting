
from datetime import datetime
import random
https: // lambdaschool.zoom.us/j/4328777428


print('type', type(datetime))

# 10 items in this list

animals = ["Duck", "Jackal", "Hippo", "Aardvark", "Cat",
           "Flamingo", "Iguana", "Giraffe", "Elephant", "Bear"]


"""
O(1) - CONSTANT TIME OPERATION
"""
# O(1) - CONSTANT TIME OPERTION
# Doesn't matter how big our list is 1 or 1mm, in order to get name of animals it's an O(1) operation
# All we're doing is one operation - returning a pointer to start of a list
# Return the name of all animals


def getAnimals():
    return animals


"""
O(n) - LINEAR operation
For every item in your input list, you do something
V common, take items and do something with it whether print it, display, make it capital, etc
Usually know you have this bc you have a FOR loop, good signifier

"""
# 0(n) - LINEAR TIME OPERATION
# As you add more inputs, the performance will increase linearly
# We initialized a number of animals to 0. We do a for loop and then return # of animals
# We have 10 animals so we're doing this count 10 times. Our input is size n and for each of these inputs we need to do something
# That something is incrementing this counter by 1
# 1 animal, do this 1 time. 1000 animals, we'd do this 1000 times
# Number of operations we need to do is linear


def countAnimals():
    num_animals = 0
    for animal in animals:
        print(f"num animals: {num_animals}")
        num_animals += 1
    return num_animals  # 10

# Now instead of doing 2 thing, we're doing two things.
# Does that mean we have O(2n)? NO - they're constants.
# & Constants get dropped. #For complexity, always drop the constants coefficients.
# All we care about is the shape of the curve is it linear, exponential, logarithmic?
# Don't care about how many operations bc there are multiple operations under the hod


# >> > countAnimals()
# num animals: 0
# num animals: 1
# num animals: 2
# num animals: 3
# num animals: 4
# num animals: 5
# num animals: 6
# num animals: 7
# num animals: 8
# num animals: 9


# O(n)
# Return each animal with all letters lowercase
# We are doing 2 operations, we have lowercase_animals, animal index.
# For each animal we increment index by one and we set new lowecase_animals to lower
def getLowercaseAnimals():
    lowercase_animals = animals
    animal_index = 0
    for animal in animals:
        lowercase_animals[animal_index] = lowercase_animals[animal_index].lower()
        animal_index += 1
    return lowercase_animals


# O(n)
# Given the name of an animal
# Return True if that animal is in the list. False otherwise
# If we have 10 operations in our list, on average we'll have to look through 5 animals assuming the item in our list
# If item is not in our list, we'll have to look through all 10
def hasAnimal(animal_name):
    num_comparisons = 0
    for animal in animals:
        num_comparisons += 1
        print(f"comparisions: {num_comparisons}")
        if animal == animal_name:
            return True
    return False


# hasAnimal("Flamingo")

# Flamingo - 6 comparisons and found out that it's true
comparisions: 1
comparisions: 2
comparisions: 3
comparisions: 4
comparisions: 5
comparisions: 6

# Dog - 10 comparisons and not true
# Duck - 1 comparison and true
# The time complexity of this is O(n) if it depends if item is in our list or not
# Best case is O(1) if item is first item in our list but doesn't really matter
# Its always worst case scenario which is O(n), every item in our list
# Average case, we look through half of our items, O(n/2) = O(0/5n) - since we dropped constant coefficient it's just O(n)
# O(n) where n is the range of 1 to the length of list
# For big O, we mean average or worst case


# O(n)
# Shuffle the order of the stored animals
# Known as fisher yates shuffling algorithm

def shuffleAnimals():
    num_animals = countAnimals()
    for i in range(num_animals):
        random_i = random.randrange(num_animals)
        temp_storage = animals[i]
        animals[i] = animals[random_i]
        animals[random_i] = temp_storage


# shuffleAnimals()
# print(animals)

"""
O(n^2)

# of operations grows v fast.
For 10 items in our list, we do 10*10 (10^2) total operations - 100. For 11 items, 121 operations.

We have O(n) with first for loop and within that we have O(n)

"""

# Print a list of all possible animal pairs
# Takes each of our animals and asks what are all the combinations we can have with each of these animals


def printAnimalPairs():
    num_operations = 0
    for animal1 in animals:
        for animal2 in animals:
            num_operations += 1
            print(f"{num_operations}: {animal1} - {animal2}")


# printAnimalPairs()


"""
O(n^3)
10*10*10 = 1000 operations
How do we know? For loop in a for loop in a for loop
10 items, 10,000 things, now our code takes 1s to run
Even if these are fast, if you have n^3 can get to performance issues

"""

# Print a list of all possible animal triples


def printAnimalTriples():
    num_operations = 0
    for animal1 in animals:
        for animal2 in animals:
            for animal3 in animals:
                num_operations += 1
                print(f"{num_operations}- {animal1} - {animal2} - {animal3}")


# printAnimalTriples()

"""
Less common

O(2^n)

O(2^nth) = power is 1042,

"""

# Given a list
# Return a list of all possible combinations of animals
# length of l should be 1024


def getListOfAnimalCombos(l):
    list_length = len(l)
    if list_length == 0:
        return [[]]
    else:
        animalCombos = []
        previousCombos = getListOfAnimalCombos(l[1:])
        for combo in previousCombos:
            animalCombos.append(combo)
            animalCombos.append(combo + [l[0]])
    return animalCombos


# l = getListOfAnimalCombos(animals)
# print(len(l))  # 1024


"""
O(n!) - n Factorial
Given a list
Return all possible arrangements of list items

10 Factorial is 10 * 9 * 8 * 7 * 5 * 4 * 3 * 2 * 1
With just an input of 10, has already exploded - you can see this takes a WHILE to load, the len is
V bad performance
"""


def getAllArrangements(l):
    list_length = len(l)
    if list_length <= 1:
        return [l]
    else:
        arrangements = []
        previousArrangements = getAllArrangements(l[1:])
        for previousArrangement in previousArrangements:
            for i in range(len(previousArrangement) + 1):
                arrangements.append(
                    previousArrangement[i:] + [l[0]] + previousArrangement[:i])
        return arrangements


l = getAllArrangements(animals)
# # print('getAllArrangements', l)
# print('len of getAllArrangements', len(l))
# len of getAllArrangements 3628800


# Given a list
# Return the list's length
# O(n)
def getLengthOfList(l):
    list_length = 0
    for i in l:
        list_length += 1
    return list_length

# Given a list
# Return the list's length
# O(1)


def betterGetLengthOfList(l):
    return len(l)


# This can be used to time the runtime of various functions
def printFunctionRuntime():
    start_time = datetime.now()
    x = getAllArrangements(animals)
    # x = getAllArrangements(animals_10) + ["Kangaroo"]
    end_time = datetime.now()
    print(end_time-start_time)


# print('Function runtime')
# printFunctionRuntime()

animals.sort()
print(animals)
