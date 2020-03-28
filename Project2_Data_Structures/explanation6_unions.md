To make the union function, I decided to use a dictionary because it allowed
me to keep track of the number of instances a given value appeared in either
of the linked lists. Therefore, no additional steps were necessary to remove
repeated values. The time complexity of the union function is O(3n), while
the space complexity is O(n), where n is the number of elements in the list.

To make the intersection function, I decided to use a list because it allowed
for storing the values that were present in both linked lists. I had to call
the set function to remove the repeated instances of values. Therefore, the
time complexity of the intersection function is O(n^2 + n), while the space
complexity is O(n), where n is the number of elements in the list. 
