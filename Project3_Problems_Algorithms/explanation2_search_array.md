<!--
@Author: otrejo
@Date:   2020-04-18T22:49:26-04:00
@Last modified by:   otrejo
@Last modified time: 2020-04-18T23:02:28-04:00
-->



# Explanation for problem 2
The data structure used is a list to keep track of indices and maintain
the data structure of the input. The algorithm chosen is a binary search
tree with recursion in order to minimize the number of passes needed
to find the number. The way this algorithm works is by checking if the
left or to the right of the mid element is increasing, and if the
target number lies between either side. If it does, then explore that side
further. If not, then explore the other side with recursion.

The time complexity is O(log(n)) and space complexity is O(n).
