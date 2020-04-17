# @Author: otrejo
# @Date:   2020-04-16T23:49:35-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-16T23:49:59-04:00



def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
   pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
