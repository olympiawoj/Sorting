[5, 9, 3, 7, 2, 8, 1, 6]

'''
1) UNDERSTAND THE PROBLEM

How to quicksort
# Pick a pivot and find the number that' higher than pivot, look from right pick first number that's higher less than pivot


[3 2 1] [5] [9 7 8 6]

Pick another pivot

L -3
R- 9

[2 1] [3] [] [5] [7 8 6] [9] []

New Pivot
L-2
R- 7

Empty- our base case, skip dont do anything
[1][2][3] [] [5] [6][7][8] [9]

Nothing - everything is now a pivot and what else has happened? Everything is in order



2) PLAN-

Two major tasks in this problem -
1) Decide on the base case
- We don't need to do anything when it's an empty array

2) Find the pivot point
3) Partitiion data to the left and right of the pivot
# Left --> smaller pivout, Right --> larger than pivot
# What if they're the same size as the pivot? Just pick one >=

# 4) Reepat, recurse!
Most expensive resource is programmer time, computing time, and memory.
If you can start better, awesome, but dont get bogged down in making something compilcated and diff to read unless you dont  need to


Two big giant tasks are a part of this
1) Doing the sort
2) Merging the arrays


Wouldnt it be two separate functions? Yes - we dont have to but its more organizes
'''

my_list = [5, 9, 3, 7, 2, 8, 1, 6]


# Divide into two functions
def partition(data):
    # Make a left list and right list
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        # Can't start at 0, slice it to skip first
        if item < pivot:
            left.append(item)
        else:
            # handling > or =
            right.append(item)
    # In python can return all 3, comma separated value - it's handling it like a tuple, doing some things for us, handled implicitly
    return left, pivot, right


def quickSort(data):
    # Base case
    # if data == []:
    if not data:
        return
    left, pivot, right = partition(data)

    # Once we have l, p, and r- we found a new pivot, which is recursion, and quicksort caling partition will happen as a result of that call
    return quickSort(left) + [pivot] + quickSort(right)

# Is this a good or bad algo? Hard to say. But go to big O cheathseet.Worst case for quicksort is On^2 whihc is pretty bad. What's the right one to use? It depends on the scenario= ultimately dpeends on what you're doing. Best sort to do solves it in one pass.


print('quicksort', quickSort(my_list)

# O(n) - this keyword
# same as for item in my_list, if item == 5, return True
# print(5 in my_list)


# # Capital true and false
# # Pair and mob programming is awesome

# # def is_it_in_here(n):
# #     for item in my_list:
# #         if item == 5:
# #             return True
# #         else:
#             return False



'''

Quicksort with list comprehensions

import random
​
def quicksort(arr):
    if arr:
        pivot = random.choice(arr)
        low = [n for n in arr if n < pivot]
        middle = [n for n in arr if n == pivot]
        high = [n for n in arr if n > pivot]
        return [*quicksort(low), *middle, *quicksort(high)]
    else:


'''
