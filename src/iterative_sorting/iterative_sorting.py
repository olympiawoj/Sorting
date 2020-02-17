
# TO-DO: Complete the selection_sort() function below

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# len is 10
"""
Selection sort segments the list into two parts - the left most is sorted, the right is unsorted

1. Search through entire list for smallest element
2. Once we find it, swap it with the first element - now we know that's sorted
3. Find smallest element of remainig items, swap with second element

i = how many values were sorted, as i increases, we check less items so j decreases
j = iterate over unsorted items, which are

i 0, check j 1-9 items
i 1, check j 2-9 items

"""


def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        # Temp variable to store position of minimum element, Assumes first element to be minimum of unsorted array
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            print(f'i: {i}, j:{j}')
            if arr[i] > arr[j]:
                # Swap found minimum el with first el
                arr[i], arr[j] = arr[j], arr[i]
    # TO-DO: swap
        print("ONE PASS COMPLETE")

    return arr


print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Loop over ever item in the array
    for i in range(0, len(arr)):
        # Repeat process for every item in array minus 1
        for j in range(0, len(arr) - i - 1):
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                # SWAP
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp
        print("ONE PASS COMPLETE")
    return arr


print(bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
