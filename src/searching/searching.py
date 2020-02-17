# STRETCH: implement Linear Search
arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


print(linear_search(arr1, 6))
print(linear_search(arr1, -6))


# def find_value_linear(sort_list, value):
#     print(sort_list)
#     for i in range(len(sort_list)):
#         print(value)
#         if sort_list[i] == value:
#             return True
#     return False


# print(find_value_linear(my_randoms, my_value))

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
