# @Author: otrejo
# @Date:   2020-03-05T17:23:35-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-05T17:48:27-05:00

# Recursive binary search using recursion
def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

# Recursion implementation
def binary_search_recursive_soln(array, target, start_index, end_index):
    # If target not in array
    if start_index > end_index:
        return -1
    # Base case
    mid_index = (start_index + end_index) // 2
    mid_value = array[mid_index]
    if mid_value == target:
        return mid_index
    elif target < mid_value:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
