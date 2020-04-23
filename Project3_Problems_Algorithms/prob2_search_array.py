#@Author: littlebigchamps
#@Date:   2020-04-08T21:23:48-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-22T21:29:23-04:00

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_recursion(input_list, number, 0, len(input_list)-1)

def rotated_array_recursion(input_list, number, start_index, end_index):
    '''

    Args:
        input_list(array), number(int), start_index (int), end_index (int)
    Returns:
        int: Index or -1
    '''
    # Base case
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2
    mid_element = input_list[mid_index]

    if mid_element == number:
        return mid_index

    left_index = rotated_array_recursion(input_list, number, start_index, mid_index-1)
    right_index = rotated_array_recursion(input_list, number, mid_index+1, end_index)

    return max(left_index, right_index)

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
