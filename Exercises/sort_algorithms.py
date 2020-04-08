# @Author: otrejo
# @Date:   2020-03-29T22:22:40-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-07T23:38:45-04:00

wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    for i in range(len(l)):
        for j in range(1, len(l)):
            if l[j-1] > l[j]:
                o_j = l[j]
                l[j] = l[j-1]
                l[j-1] = o_j


bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for i in range(len(l)):
        for j in range(1, len(l)):
            this_h = l[j][0]
            this_m = l[j][1]
            prev_h = l[j-1][0]
            prev_m = l[j-1][1]

            if prev_h > this_h:
                continue

            elif prev_h == this_h and prev_m > prev_m:
                continue

            l[j] = (prev_h, prev_m)
            l[j-1] = (this_h, this_m)


bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")

def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
            print(right_index)
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))

# Case sort
def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    # Sort string
    sort_string = sorted(string)
    index = 0
    for letter in sort_string:
        num = ord(letter)
        if num >= 97:
            break
        index += 1

    lower = sort_string[index:]
    upper = sort_string[:index]

    # Create output
    output = []

    # Iterate over string
    i_lower = 0
    i_upper = 0
    for char in string:
        if ord(char) >= 97:
            output.append(lower[i_lower])
            i_lower += 1

        else:
            output.append(upper[i_upper])
            i_upper += 1

    return ''.join(output)

def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")

test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
