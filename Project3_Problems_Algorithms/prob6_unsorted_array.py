# @Author: otrejo
# @Date:   2020-04-16T23:49:35-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-05-02T20:28:39-04:00



def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # Compare first two integers
    if len(ints) == 0:
        return None

    if ints[0] < ints[1]:
        min_int = ints[0]
        max_int = ints[1]
    else:
        min_int = ints[1]
        max_int = ints[0]

    for i in range(2, len(ints)):
        if ints[i] < min_int:
            min_int = ints[i]
        elif ints[i] > max_int:
            max_int = ints[i]
        else:
            continue

    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") # Pass
print ("Pass" if ((0, 8) == get_min_max(l)) else "Fail") # Fail

l = [0, 0, 0, 0, 0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail") # Pass
print ("Pass" if ((0, 1) == get_min_max(l)) else "Fail") # Fail

# Edge cases
l = []
print ("Pass" if (None == get_min_max(l)) else "Fail") # Pass
l = [10000, 0.0000001, 1000, 0.01]
print ("Pass" if ((0.0000001, 10000) == get_min_max(l)) else "Fail") # Pass
