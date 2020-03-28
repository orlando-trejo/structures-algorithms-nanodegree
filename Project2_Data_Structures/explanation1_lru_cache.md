To make a Least Recently Used (LRU) data structure, I decided to use
the OrderedDict from Python. OrderedDict is a subclass that remembers
the order entries were added, which is necessary for implementing an
LRU cache. Furthermore, by using a dictionary data structure it is
possible to introduce to put and get entries with time complexity of O(1).
Space complexity is O(n), where n is the number of elements in the cache.
