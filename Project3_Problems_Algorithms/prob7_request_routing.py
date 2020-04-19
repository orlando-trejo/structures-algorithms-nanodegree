# @Author: otrejo
# @Date:   2020-04-17T18:33:31-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-04-18T22:22:27-04:00



# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        print(path_list)
        for path in path_list:
            current_node.children[path] = RouteTrieNode()
            current_node = current_node.children[path]

        current_node.handler = handler


    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        print(path_list)
        for path in path_list:
            if current_node.children[path]:
                continue
            else:
                return None
        return "/".join(path_list)

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, handler):
        # Insert the node as before
        self.children[handler] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the path parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.trie.insert(path_list, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.trie.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split("/")[1:]

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler")#, "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
#print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one