from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict() # Use ordered dict as doubly linked list

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        else:
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
            return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False) # FIFO
        self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.cache)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.cache)


our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.cache)


print(our_cache.get(3))
print(our_cache.cache)
