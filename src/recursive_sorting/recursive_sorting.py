# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    if elements <= 0:
        return

    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO

    # Our while loop runs while i and j are less than len of their array
    i = 0
    j = 0

    while (i < len(arrA)) and (j < len(arrB)):
        # Compare results and push
        # If this is the case, i will no longer be 0 so move i up by 1
        if(arrB[j] > arrA[i]):
            merged_arr.append(arrA[i])
            i += 1
        else:
            # Equality case when When arrA is greater
            merged_arr.append(arrB[j])
            j += 1
    # If we hit the end of an array, push all remaining values from other array
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1

    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


def merge2(listA, listB):
    elements = len(listA) + len(listB)
    merged_arr = []

    # Elements is len of A + B

    for i in range(elements):
        if len(listA) == 0:
            merged_arr.append(listB[0])
            listB = listB[1:]
        elif len(listB) == 0:
            merged_arr.append(listA[0])
            listA = listA[1:]
        elif listA[0] < listB[0]:
            merged_arr.append(listA[0])
            listA = listA[1:]
        else:
            merged_arr.append(listB[0])
            listB = listB[1:]
    return merged_arr


"""
Print Tests

print(merge([1, 10, 50], [2, 14, 99, 100]))
# merged arr [1, 10, 50, 2, 14, 99, 100]
print(merge([100], [1, 3, 4, 5]))
# works(5) [1, 3, 4, 5, 100]

print(merge([], [1, 3]))
# (2) [1, 3] - works bc first loop does not run

print(merge([1, 2, 3], [2, 3, 4]))

"""

# TO-DO: implement the Merge Sort function below USING RECURSION
'''
Objective: Break up array into halfs until you have arrays that are empty or have one element
- Find the mid by dividing length by 2 and floorig ing it
- Array of 0 or 1 elements are sorted
- Use array.slice to break up array
Base Case: If the length of the arr is <=1, then it is sorted

'''


def merge_sort(arr):
    # TO-DO
    # What's our base case? If the length of the arr is <=1
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # call merge sort recursively on two halfs of array
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge the left and right
    return merge(left, right)


print(merge_sort([10, 24, 76, 73, 72, 1, 9]))


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

# def timsort(arr):

# return arr
