# @Author: otrejo
# @Date:   2020-06-28T22:39:09-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-07-03T20:48:42-04:00


import numpy as np

def get_distance(coords, pos_i, pos_f):
    vec_i = np.array(coords[pos_i])
    vec_f = np.array(coords[pos_f])
    return np.linalg.norm(vec_f - vec_i)


def shortest_path(roads, intersections, start, goal):

    lookup_table = np.array([[start], np.inf])
    path = [start]

    for road in roads[start]:
        g = get_distance(intersections, start, road)
        h = get_distance(intersections, road, goal)
        f = g + h
        print([[start, road], g, h, f])
        lookup_table = np.vstack((lookup_table, [[start, road], f]))


    min_i = np.argmin(lookup_table[:,1])
    path.append(lookup_table[min_i][0][-1])

    while goal not in lookup_table[min_i][0]:
        start = lookup_table[min_i][0][-1]
        for road in roads[start]:
            g = get_distance(intersections, start, road)
            h = get_distance(intersections, road, goal)
            f = g + h
            print([[start, road], g, h, f])
            lookup_table = np.vstack((lookup_table, [[start, road], f]))

        # Redefine min_i
        min_i = np.argmin(lookup_table[:,1])
        path.append(lookup_table[min_i][0][-1])

    print(path)
    return

# Code from Red Blob Games on A* Search
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


roads = [[36, 34, 31, 28, 17],
         [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
         [39, 36, 21, 19, 9, 7, 4],
         [35, 20, 15, 11, 6],
         [39, 36, 21, 19, 9, 7, 2],
         [32, 16, 14],
         [35, 20, 15, 11, 1, 3],
         [39, 36, 22, 21, 19, 9, 2, 4],
         [33, 30, 14],
         [36, 21, 19, 2, 4, 7],
         [31, 27, 26, 25, 24, 18, 17, 13],
         [35, 20, 15, 3, 6],
         [37, 34, 31, 28, 22, 17],
         [27, 24, 18, 10],
         [33, 30, 16, 5, 8],
         [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
         [37, 30, 5, 14],
         [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
         [31, 27, 26, 25, 24, 1, 10, 13, 17],
         [21, 2, 4, 7, 9],
         [35, 26, 1, 3, 6, 11, 15],
         [2, 4, 7, 9, 19],
         [39, 37, 29, 7, 12],
         [38, 32, 29],
         [27, 10, 13, 18],
         [34, 31, 27, 26, 1, 10, 15, 17, 18],
         [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
         [31, 1, 10, 13, 18, 24, 25, 26],
         [39, 36, 34, 31, 0, 12, 17],
         [38, 37, 32, 22, 23],
         [33, 8, 14, 16],
         [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
         [38, 5, 23, 29],
         [8, 14, 30],
         [0, 12, 17, 25, 26, 28, 31],
         [1, 3, 6, 11, 15, 20],
         [39, 0, 2, 4, 7, 9, 28],
         [12, 16, 22, 29],
         [23, 29, 32],
         [2, 4, 7, 22, 28, 36]]

intersections = {0: [0.7801603911549438, 0.49474860768712914],
                 1: [0.5249831588690298, 0.14953665513987202],
                 2: [0.8085335344099086, 0.7696330846542071],
                 3: [0.2599134798656856, 0.14485659826020547],
                 4: [0.7353838928272886, 0.8089961609345658],
                 5: [0.09088671576431506, 0.7222846879290787],
                 6: [0.313999018186756, 0.01876171413125327],
                 7: [0.6824813442515916, 0.8016111783687677],
                 8: [0.20128789391122526, 0.43196344222361227],
                 9: [0.8551947714242674, 0.9011339078096633],
                 10: [0.7581736589784409, 0.24026772497187532],
                 11: [0.25311953895059136, 0.10321622277398101],
                 12: [0.4813859169876731, 0.5006237737207431],
                 13: [0.9112422509614865, 0.1839028760606296],
                 14: [0.04580558670435442, 0.5886703168399895],
                 15: [0.4582523173083307, 0.1735506267461867],
                 16: [0.12939557977525573, 0.690016328140396],
                 17: [0.607698913404794, 0.362322730884702],
                 18: [0.719569201584275, 0.13985272363426526],
                 19: [0.8860336256842246, 0.891868301175821],
                 20: [0.4238357358399233, 0.026771817842421997],
                 21: [0.8252497121120052, 0.9532681441921305],
                 22: [0.47415009287034726, 0.7353428557575755],
                 23: [0.26253385360950576, 0.9768234503830939],
                 24: [0.9363713903322148, 0.13022993020357043],
                 25: [0.6243437191127235, 0.21665962402659544],
                 26: [0.5572917679006295, 0.2083567880838434],
                 27: [0.7482655725962591, 0.12631654071213483],
                 28: [0.6435799740880603, 0.5488515965193208],
                 29: [0.34509802713919313, 0.8800306496459869],
                 30: [0.021423673670808885, 0.4666482714834408],
                 31: [0.640952694324525, 0.3232711412508066],
                 32: [0.17440205342790494, 0.9528527425842739],
                 33: [0.1332965908314021, 0.3996510641743197],
                 34: [0.583993110207876, 0.42704536740474663],
                 35: [0.3073865727705063, 0.09186645974288632],
                 36: [0.740625863119245, 0.68128520136847],
                 37: [0.3345284735051981, 0.6569436279895382],
                 38: [0.17972981733780147, 0.999395685828547],
                 39: [0.6315322816286787, 0.7311657634689946]}

print(get_distance(intersections, 8, 33))
print(get_distance(intersections, 8, 30))
print(get_distance(intersections, 8, 14))
print(get_distance(intersections, 33, 24))
print(get_distance(intersections, 30, 24))
print(get_distance(intersections, 14, 24))

print('next round')
print(get_distance(intersections, 16, 37))
print(get_distance(intersections, 16, 30))
print(get_distance(intersections, 16, 5))
print(get_distance(intersections, 16, 14))
print(get_distance(intersections, 37, 34))
print(get_distance(intersections, 30, 34))
print(get_distance(intersections, 5, 34))
print(get_distance(intersections, 14, 34))

print('next round')
print(get_distance(intersections, 12, 37))
print(get_distance(intersections, 12, 34))
print(get_distance(intersections, 12, 31))
print(get_distance(intersections, 12, 28))
print(get_distance(intersections, 12, 22))
print(get_distance(intersections, 12, 17))
print(get_distance(intersections, 37, 34))
print(get_distance(intersections, 34, 34))
print(get_distance(intersections, 31, 34))
print(get_distance(intersections, 28, 34))
print(get_distance(intersections, 22, 34))
print(get_distance(intersections, 17, 34))


import math
from queue import PriorityQueue


roads = [[36, 34, 31, 28, 17],
         [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
         [39, 36, 21, 19, 9, 7, 4],
         [35, 20, 15, 11, 6],
         [39, 36, 21, 19, 9, 7, 2],
         [32, 16, 14],
         [35, 20, 15, 11, 1, 3],
         [39, 36, 22, 21, 19, 9, 2, 4],
         [33, 30, 14],
         [36, 21, 19, 2, 4, 7],
         [31, 27, 26, 25, 24, 18, 17, 13],
         [35, 20, 15, 3, 6],
         [37, 34, 31, 28, 22, 17],
         [27, 24, 18, 10],
         [33, 30, 16, 5, 8],
         [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
         [37, 30, 5, 14],
         [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
         [31, 27, 26, 25, 24, 1, 10, 13, 17],
         [21, 2, 4, 7, 9],
         [35, 26, 1, 3, 6, 11, 15],
         [2, 4, 7, 9, 19],
         [39, 37, 29, 7, 12],
         [38, 32, 29],
         [27, 10, 13, 18],
         [34, 31, 27, 26, 1, 10, 15, 17, 18],
         [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
         [31, 1, 10, 13, 18, 24, 25, 26],
         [39, 36, 34, 31, 0, 12, 17],
         [38, 37, 32, 22, 23],
         [33, 8, 14, 16],
         [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
         [38, 5, 23, 29],
         [8, 14, 30],
         [0, 12, 17, 25, 26, 28, 31],
         [1, 3, 6, 11, 15, 20],
         [39, 0, 2, 4, 7, 9, 28],
         [12, 16, 22, 29],
         [23, 29, 32],
         [2, 4, 7, 22, 28, 36]]

intersections = {0: [0.7801603911549438, 0.49474860768712914],
                 1: [0.5249831588690298, 0.14953665513987202],
                 2: [0.8085335344099086, 0.7696330846542071],
                 3: [0.2599134798656856, 0.14485659826020547],
                 4: [0.7353838928272886, 0.8089961609345658],
                 5: [0.09088671576431506, 0.7222846879290787],
                 6: [0.313999018186756, 0.01876171413125327],
                 7: [0.6824813442515916, 0.8016111783687677],
                 8: [0.20128789391122526, 0.43196344222361227],
                 9: [0.8551947714242674, 0.9011339078096633],
                 10: [0.7581736589784409, 0.24026772497187532],
                 11: [0.25311953895059136, 0.10321622277398101],
                 12: [0.4813859169876731, 0.5006237737207431],
                 13: [0.9112422509614865, 0.1839028760606296],
                 14: [0.04580558670435442, 0.5886703168399895],
                 15: [0.4582523173083307, 0.1735506267461867],
                 16: [0.12939557977525573, 0.690016328140396],
                 17: [0.607698913404794, 0.362322730884702],
                 18: [0.719569201584275, 0.13985272363426526],
                 19: [0.8860336256842246, 0.891868301175821],
                 20: [0.4238357358399233, 0.026771817842421997],
                 21: [0.8252497121120052, 0.9532681441921305],
                 22: [0.47415009287034726, 0.7353428557575755],
                 23: [0.26253385360950576, 0.9768234503830939],
                 24: [0.9363713903322148, 0.13022993020357043],
                 25: [0.6243437191127235, 0.21665962402659544],
                 26: [0.5572917679006295, 0.2083567880838434],
                 27: [0.7482655725962591, 0.12631654071213483],
                 28: [0.6435799740880603, 0.5488515965193208],
                 29: [0.34509802713919313, 0.8800306496459869],
                 30: [0.021423673670808885, 0.4666482714834408],
                 31: [0.640952694324525, 0.3232711412508066],
                 32: [0.17440205342790494, 0.9528527425842739],
                 33: [0.1332965908314021, 0.3996510641743197],
                 34: [0.583993110207876, 0.42704536740474663],
                 35: [0.3073865727705063, 0.09186645974288632],
                 36: [0.740625863119245, 0.68128520136847],
                 37: [0.3345284735051981, 0.6569436279895382],
                 38: [0.17972981733780147, 0.999395685828547],
                 39: [0.6315322816286787, 0.7311657634689946]}


import math
from queue import PriorityQueue

def measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def generatePath(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path

def shortest_path(roads, intersections, start, goal):
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)

    prev = {start: None}
    score = {start: 0}
    #print(prev, score)
    while not pathQueue.empty():
        print(pathQueue)
        #print(prev, score)
        curr = pathQueue.get()
        #print(curr)
        if curr == goal:
            generatePath(prev, start, goal)

        for node in roads[curr]:
            #print(node)
            update_score = score[curr] + \
                measure(intersections[curr], intersections[node])

            if node not in score or update_score < score[node]:
                score[node] = update_score
                totalScore = update_score + \
                    measure(intersections[curr],
                            intersections[goal])
                pathQueue.put(node, totalScore)
                prev[node] = curr
    print(prev, score)
    return generatePath(prev, start, goal)

print(shortest_path(roads, intersections, 5, 34))
