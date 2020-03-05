# DoubleNode Class
class DoubleNode(object):
    """Connections forward and backwards through list."""

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


# DoublyLinkedList Class
class DoublyLinkedList(object):
    """Keep track of head and tail in list."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        # Create new node
        node = DoubleNode(value)

        # Check if a head already exists
        if self.head is None:
            self.head = node
            self.tail = self.head
        # If not empty, make new node tail
        else:
            old_tail = self.tail
            old_tail.next = node
            self.tail = node
            self.tail.prev = tail
        # Update count
        self.count += 1



    def remove_from_list(self, node):
        saved_prev = node.prev
        saved_next = node.next

        saved_prev.next = saved_next
        saved_next.prev = saved_prev

    def remove_from_tail(self, node):
        self.tail = node.prev
        self.tail.next = None
        return node.value

    def add_to_front(self, node):
        # If there is no head
        if self.head is None:
            self.head = node
            self.tail = node
        else: # If there is a head
            self.head.prev = node
            node.next = self.head
            self.head = node
        return node

    def move_to_front(self, key, node):
        # Check if node is head
        if self.head == node:
            return
        if self.tail == node:
            self.remove_from_tail(node)
        else:
            self.remove_from_list(node)
        return add_to_front(node)



# LRU Cache Class
class LRU_cache(object):
    """docstring for LRU_cache."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = {}
        self.num_elements = 0
        self.dllist = DoublyLinkedList()


    def get(self, key):
        # Retrieve item given key. Return -1 if nonexistent.
        if key not in self.hashtable:
            return -1
        else:
            # Return value and update ddlist
            self.ddlist.move_to_front()
            return self.hashtable[key]


    def set(self, key, value):
        node = self.hashtable[key]

        if node is None:
            new_node = DoubleNode(value)
            new_node.key = key
            new_node.value = value

            self.hashtable[key] = value

            self.move_to_front(new_node)

            self.num_elements += 1

            if self.num_elements > self.capacity:
