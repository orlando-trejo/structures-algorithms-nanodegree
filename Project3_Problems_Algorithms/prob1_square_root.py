# @Author: littlebigchamps
# @Date:   2020-04-08T21:15:05-04:00
# @Last modified by:   littlebigchamps
# @Last modified time: 2020-04-08T21:22:26-04:00

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    index = 0

    while index * index < number:
        index += 1

    if index * index > number:
        return index - 1
    else:
        return index

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
