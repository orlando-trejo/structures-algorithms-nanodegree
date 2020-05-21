# @Author: otrejo
# @Date:   2020-05-04T22:59:30-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-05-20T22:21:41-04:00

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


# Connecting islands
import heapq

# Function to create graph
def create_graph(num_islands, bridge_config):
    # Initiate list of lists (adjacency list)
    graph = [list() for _ in range(num_islands+1)]

    # Create graph
    for config in bridge_config:
        i_island = config[0]
        f_island = config[1]
        cost = config[2]
        graph[i_island].append((f_island, cost))
        graph[f_island].append((i_island, cost))

    return graph

# Minimize cost
def get_minimum_cost(graph):
    # Start vertex
    vertex = 1
    # Visited vertices
    visited = [False for _ in range(len(graph))]
    # Initialize heap
    heap = [(0, vertex)]
    total_cost = 0

    while len(heap) > 0:
        cost, current_vertex = heapq.heappop(heap)

        if visited[current_vertex]:
            continue

        total_cost += cost

        for island, cost in graph[current_vertex]:
            heapq.heappush(heap, (cost, island))

        visited[current_vertex] = True

    return total_cost

# Get minimum cost
def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return get_minimum_cost(graph)

# Test function
def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")

# Test case 1
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# Test case 2
num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# Test case 3
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
