# @Author: otrejo
# @Date:   2020-05-04T22:59:30-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-05-20T17:58:23-04:00

# Do a depth first search on a graph

# Create graph class
class GraphNode(object):

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):

    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

def dfs_search(root_node, search_value):
    visit_odrer = list()
    stack = [root_node]

    while len(stack) > 0:
        node = stack.pop()
        visit_odrer.append(node)

        if node.value() == search_value:
            return node

        for child in node.children:
            if child not in visit_order:
                stack.append(child)

# Implement recursion DFS
def dfs_recursion_start(self, start_node):
    visited = {}
    self.dfs_recursion(start_node, visited)

def dfs_recursion(self, node, visited):
    if node == None:
        return False

    visited[node.value] = True
    print(node.value)

    for child in node.children:
        if child.value not in visited:
            self.dfs_recursion(child, visited)

Graph.dfs_recursion_start = dfs_recursion_start

Graph.dfs_recursion = dfs_recursion

graph1.dfs_recursion_start(nodeG)

# Implment BFS search
def bfs_search(root_node, search_value):
    visited = list()
    queue = [root_node]

    while len(queue) > 0:
        node = queue.pop(0)
        visited.append(node)

    if node.value == search_value:
        return node

    for child in node.children:
        if child not in visited:
            queue.append(child)

# Diijkstra's Algorithm
class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, node):
        if node in self.edges:
            self.edges.remove(node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

# Create Graph
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_u, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_u, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_d, 4)
graph.add_edge(node_c, node_u, 6)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_a, 7)
graph.add_edge(node_i, node_c, 4)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_c, 5)
graph.add_edge(node_t, node_y, 5)
graph.add_edge(node_y, node_i, 4)
graph.add_edge(node_y, node_t, 5)

#Implementation Diijkstra's algorithm
import math

def dijkstra(start_node, end_node, graph):
    # Initialize dictionary with inf for distances
    distances = {node: math.inf for node in graph.nodes}
    short_paths = {}
    distances[start_node] = 0
    while distances:
        current_node, node_distance = sorted(distances.items(), key=lambda x: x[1])[0]
        short_paths[current_node] = distances.pop(current_node)
        for edge in current_node.edges:
            if edge.node in distances:
                new_node_distance = node_distance + edge.distance
                if new_node_distance < distances[edge.node]:
                    distances[edge.node] = new_node_distance

    return short_paths[end_node]

print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y, graph)))
