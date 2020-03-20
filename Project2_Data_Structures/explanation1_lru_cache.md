Why use the data structure? What is the efficiency?
To make a Least Recently Used (LRU) data structure, I decided to use
the OrderedDict from Python. OrderedDict is a subclass that remembers
the order entries were added, which is necessary for implementing an
LRU cache. Furthermore, by using a dictionary data structure it is
possible to introduce to put and get entries with time complexity of O(1). 
