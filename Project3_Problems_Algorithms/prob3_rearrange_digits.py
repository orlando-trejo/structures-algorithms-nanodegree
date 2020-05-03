# @Author: otrejo
# @Date:   2020-04-11T23:28:21-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-05-02T19:41:57-04:00


# Implement quick sort algorithm w/ recursion
def quick_sort(input_list):
    return quick_sort_recursion(input_list, 0, len(input_list)-1)

def quick_sort_recursion(input_list, start_index, end_index):

    # Base case
    if start_index > end_index:
        return

    pivot_index = partial_sort(input_list, start_index, end_index)

    quick_sort_recursion(input_list, start_index, pivot_index-1)
    quick_sort_recursion(input_list, pivot_index+1, end_index)

def partial_sort(input_list, start_index, end_index):
    right_index = end_index
    pivot_index = start_index
    pivot_value = input_list[pivot_index]

    while (pivot_index != right_index):

        item = input_list[right_index]

        if item <= pivot_value:
            right_index -= 1
            continue

        input_list[right_index] = input_list[pivot_index+1]
        input_list[pivot_index+1] = pivot_value
        input_list[pivot_index] = item
        pivot_index += 1

    return pivot_index

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quick_sort(input_list)
    print(input_list)
    num1 = ''
    num2 = ''
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 += str(input_list[i])
        else:
            num2 += str(input_list[i])

    return [int(num1), int(num2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]]) # Pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case) # Pass
test_case = [[4, 6, 4, 5, 9, 8], [964, 852]]
test_function(test_case) # Fail

# Edge cases
test_case = [[1, 1, 1, 1, 1, 1, 1], [1111, 111]]
test_function(test_case) # Pass
test_case = [[9,7,5,3,1,3,2,4,5],[95431, 7532]]
test_function(test_case) # Pass
