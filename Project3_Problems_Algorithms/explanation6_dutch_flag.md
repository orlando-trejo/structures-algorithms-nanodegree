<!--
@Author: otrejo
@Date:   2020-04-18T23:03:28-04:00
@Last modified by:   otrejo
@Last modified time: 2020-04-18T23:03:34-04:00
-->



# Explanation for problem 6
Used lists to keep track of indices. This algorithm checks that input list
has length 0. If so, it returns 'None'. If not, then it continues to determine
initial values for the minimum and maximum values. Then it proceeds along the
list to compare the minimum and maximum current values. If the current value is
lower than the current minimum value, then it becomes the new minimum value.
Similarly, if the current values is larger than the maximum value, then it 
becomes the new maximum value.

Time complexity is O(n) and space complexity is O(2).
