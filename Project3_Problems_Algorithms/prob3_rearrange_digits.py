# @Author: otrejo
# @Date:   2020-04-11T23:28:21-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-12T23:21:45-04:00


def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    for i in range(len(l)):
        for j in range(1, len(l)):
            if l[j-1] < l[j]:
                o_j = l[j]
                l[j] = l[j-1]
                l[j-1] = o_j
    return l


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = bubble_sort_1(input_list)
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

print(rearrange_digits([1, 2, 3, 4, 5]))

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
