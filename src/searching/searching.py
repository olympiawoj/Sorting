# STRETCH: implement Linear Search
arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


print(linear_search(arr1, 6))
print(linear_search(arr1, -6))


# print(find_value_linear(my_randoms, my_value))

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    found = False  # A flag
    print('sorted arr', arr)

    while low <= high and not found:
        middle = ((low + high)//2)
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1  # not found


arr2 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr2, -8))
# Should return 1

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
