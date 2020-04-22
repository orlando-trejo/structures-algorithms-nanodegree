#@Author: littlebigchamps
#@Date:   2020-04-08T21:23:48-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-21T22:57:04-04:00

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Base case
    if len(input_list) == 0:
        return -1

    mid_index = len(input_list) // 2
    left_side = input_list[0:mid_index]
    right_side = input_list[mid_index:]
    if number >= left_side[0]:
        return linear_search(left_side, number)
    else:
        return linear_search(right_side, number) + len(left_side)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Pass
# Edge cases
test_function([[], 10]) # Pass
test_function([[1, 1, 1, 1, 1, 1, 1], 1]) # Pass
