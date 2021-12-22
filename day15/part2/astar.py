import sys
from queue import PriorityQueue

class AStar:
    def __init__(self, costs):
        self.costs = costs
        self.height = len(costs)
        self.width = len(costs[0])

        self.nodes = [[Node() for i in range(self.width)] for j in range(self.height)]

        self.start = [0,0]
        self.goal = [self.height-1, self.width-1]

        self.open = PriorityQueue()

        start = self.get_node(self.start)
        start.G = 0
        start.F = self.heuristic(self.start)

        self.open.put((start.F, self.start))

    def heuristic(self, coords):
        g = self.goal
        return (g[0]-coords[0]) + (g[1]-coords[1])

    def get_cost(self, coords):
        return self.costs[coords[0]][coords[1]]

    def get_node(self, coords):
        return self.nodes[coords[0]][coords[1]]

    def get_neighbors(self, coords):
        arr = []
        if coords[0] > 0:
            arr.append([coords[0]-1, coords[1]])
        if coords[0] < self.height-1:
            arr.append([coords[0]+1, coords[1]])
        if coords[1] > 0:
            arr.append([coords[0], coords[1]-1])
        if coords[1] < self.width-1:
            arr.append([coords[0], coords[1]+1])
        return arr

    def run(self):
        while not self.open.empty():
            current_coords = self.open.get()[1]
            current = self.get_node(current_coords)

            if current_coords == self.goal:
                return current.G

            for neighbor_coords in self.get_neighbors(current_coords):
                neighbor = self.get_node(neighbor_coords)

                possible_g = current.G + self.get_cost(neighbor_coords)
                if possible_g < neighbor.G:
                    neighbor.cameFrom = current
                    neighbor.G = possible_g
                    neighbor.F = possible_g + self.heuristic(neighbor_coords)
                    if neighbor not in self.open.queue:
                        self.open.put((neighbor.F, neighbor_coords))
        return None

class Node:
    def __init__(self):
        self.G = sys.maxsize
        self.F = sys.maxsize
        self.cameFrom = None
