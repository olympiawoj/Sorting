import random

my_range = 10000000
size = 10000000

my_randoms = random.sample(range(my_range), size)

my_value = random.randint(0, my_range)


# # A linear search algo
# def find_value_linear(sort_list, value):
#     print(sort_list)
#     for i in range(len(sort_list)):
#         print(value)
#         if sort_list[i] == value:
#             return True
#     return False


# print(find_value_linear(my_randoms, my_value))


# HOW Can we make the above better? let's turn it into binary
# Step 1, sort it
my_randoms.sort

# Step 2, binary search - must be sorted for this to work
# Still takes a long time - why? thought it was supposed to make it better?

#


def find_value_binary(sort_list, value):
    # Edge case - if list is empty, return false
    if len(sort_list) == 0:
        return False
    first = 0
    # 0 index so len list is 1 biggger than index number of last
    last = len(sort_list) - 1

    found = False  # A flag

    # Loop until found, or check everything
    while first <= last and not found:
        # Find middle of list using integer division //
        # Use first because it's going to change with the section we're searching, we want to find middle of each individual section which we slowly narrow down
        middle = (first + last // 2)

        # if middle of subarray we're sorting equals our value, set found = true
        if sort_list[middle] == value:
            found = true
        else:
            # Search lower half
            if value < sort_list[middle]:
                # Last is updated to BELOW the middle one, 1 less than last
                last = middle - 1
            else:
                # Search upper half
                first = middle + 1
        return found


# What happens here is that, first one takes the longest, bc sorting uses up a lot of computation
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))
print(find_value_binary(my_randoms, my_value))


# We're not just doing a search, we're doing a sort. Once we sorted, it's MUCH faster, but the sort itself took time - this is a caveat with binary search.
# What's the best way to solve this problem if you're able to?? Keep the list sorted, build sorting into keeping that list when you add something new to the list, add it in then
# But it ultimately depends, design your algos for the circimstance
