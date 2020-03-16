# @Author: code adapted or used from Udacity
# @Date:   2020-03-05T17:23:35-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-15T22:37:51-04:00

# Recursive binary search using recursion
def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

# Recursion implementation
def binary_search_recursive_soln(array, target, start_index, end_index):
    # If target not in array
    if start_index > end_index:
        return -1
    # Base case
    mid_index = (start_index + end_index) // 2
    mid_value = array[mid_index]
    if mid_value == target:
        return mid_index
    elif target < mid_value:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)

# Test function for binary search recursion function
def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print('Pass!')
    else:
        print('Fail!')

# Test case
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case) # Should return "Pass!"

# Variation on binary search
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)

# Find first instance
def find_first(target, source):
    i_pos = recursive_binary_search(target, source)
    if not i_pos:
        return -1
    while source[i_pos] == target:
        n_pos = i_pos - 1
        if i_pos == 0:
            return 0
        elif source[n_pos] == target:
            i_pos = n_pos
        else:
            return i_pos

# Test find first
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple)) # Should return 3
print(find_first(9, multiple)) # Should return None

# Determine if source contains target
def contains(target, source):
    if recursive_binary_search(target, source) is None:
        return False
    else:
        return True

# Test contains
letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False

# Find start index
def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)

# Find end index
def find_end_index(arr, number, start_index, end_index):
    # binary search to find last target index in the array
    if end_index < start_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos

    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)




# Find first and last index of target in source
def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index
    first_index = find_start_index(arr, number, 0, len(arr) - 1)
    last_index = find_end_index(arr, number, 0, len(arr) - 1)

    return [first_index, last_index]

# Test function
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)

# Tries
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True


    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]
        return current_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
# Heap class
class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * (parent_index + 1)
            right_child_index = 2 * (parent_index + 2)

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

# Test Heap
heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))

print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))

# Node class for Red-Black Tree
class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

# Red-Black Tree Class
class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_value:
            if current.right:
                insert_helper(current.right, current, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                insert_helper(current.left, current, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        # Case 1
        if node.parent == None:
            return
        # Case 2
        if node.parent.color = 'black':
            return
        # Case 3
        if pibling(node).color == 'red':
            pibling(node).color == 'black'
            node.parent.color == 'black'
            grandparent(node).color == 'red'
            self.rebalance(grandparent(node))
        # Case 4
        gp = grandparent(node)
        if gp.left and node == gp.left.right:
            self.rotate_left(parent(node))
        if gp.right and node = gp.right.left:
            self.rotate_right(parent(node))
        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_left(gp)
        else:
            self.rotate_right(gp)
        p.color = 'black'
        gp.color = 'red'

    # Rotate left method
    def rotate_left(self, node):
        # Original parent node
        p = node.parent
        # Node moving up
        node_moving_up = node.right
        # After moving, right child is left child
        node.right = node_moving_up.left
        # Node moves down to be left child
        node_moving_up.left = node
        node.parent = node_moving_up
        # Connect to sub-tree parent, node may have been root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    # Rotate right method
    def rotate_right(self, node):
        # Original parent node
        p = node.parent
        # Node moving up
        node_moving_up = node.left
        # After moving, left child is right child
        node.left = node_moving_up.right
        # Node moves down to be right child
        node_moving_up.right = node
        node.parent = node_moving_up
        # Connect to sub-tree parent, node may have been root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def remove(self, find_val):
        return False
