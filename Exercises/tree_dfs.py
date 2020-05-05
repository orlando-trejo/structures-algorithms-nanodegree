# @Author: otrejo
# @Date:   2020-05-04T22:23:32-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-05-04T22:48:49-04:00



# Notes from Udacity course

# Make node for tree and tree
class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

class Tree():

    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

# Create a tree and some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# Make stack to keep track of tree nodes during traversal
class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n____________\n"
            s += "\n____________\n".join([str(item) for item in self.list[::-1]])
            s += "\n____________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"

# Check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack)
