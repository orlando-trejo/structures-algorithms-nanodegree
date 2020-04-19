# @Author: otrejo
# @Date:   2020-04-11T23:47:12-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-18T22:58:51-04:00



def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zeros = []
    ones = []
    twos = []
    for i in input_list:
        if i == 0:
            zeros.append(0)
        elif i == 1:
            ones.append(1)
        else:
            twos.append(2)

    return zeros + ones + twos

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) #Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #Pass
