# @Author: otrejo
# @Date:   2020-04-11T23:47:12-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-05-02T20:18:38-04:00



def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0_index = 0
    next_2_index = len(input_list) - 1
    moving_index = 0

    while (moving_index <= next_2_index):
        if input_list[moving_index] == 0:
            input_list[moving_index] = input_list[next_0_index]
            input_list[next_0_index] = 0
            moving_index += 1
            next_0_index += 1
        elif input_list[moving_index] == 2:
            input_list[moving_index] = input_list[next_2_index]
            input_list[next_2_index] = 2
            next_2_index -= 1
        else:
            moving_index += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) #Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #Pass

# Edge cases
test_function([0, 0, 0, 0, 0, 0]) #Pass
test_function([2, 2, 2, 2, 2, 2]) #Pass
test_function([]) #Pass
