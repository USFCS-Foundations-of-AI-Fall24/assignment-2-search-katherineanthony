import math
from queue import PriorityQueue

from Graph import Graph, Edge


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = read_mars_graph("MarsMap")
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((start_state.f, start_state))
    mars_graph = start_state.mars_graph
    states_generated = 0

    closed_list[start_state] = True
    while search_queue.qsize() > 0 :
        next_state = search_queue.get()
        if goal_test(next_state[1]):
            print(next_state[1])
            print("states_generated: ", states_generated)
            print("Goal found with f:", next_state[0])
            return next_state[1]
        else :
            edges = mars_graph.get_edges(next_state[1].location)
            for e in edges :
                g = next_state[1].g + 1
                h = heuristic_fn(e.dest)
                m = map_state(location=e.dest, prev_state=next_state[1], g=g, h=h)
                f = g + h
                if m not in closed_list :
                    search_queue.put((f, m))
                    closed_list[m] = True
                    states_generated += 1



## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    coordinates = ""
    try :
        coordinates = state.split(",")
    except:
        coordinates = state.location.split(",")
    return math.sqrt(pow(int(coordinates[0]) - 1, 2) + pow(int(coordinates[1]) - 1, 2))

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    # once we have the number of nodes, add that here
    graph = Graph()
    with open(filename) as f:
        for line in f.readlines():
            content = line.split()
            content[0] = content[0].strip(":")
            graph.add_node(content[0])
            for edge in content[1:]:
                e = Edge(content[0], edge)
                graph.add_edge(e)

    return graph

def g(s):
    return s.location == "1,1"

def main():
    map = map_state(location="4,4")
    print("testing heuristic function...")
    a_star(map, h1, g)

    print("------------------")

    print("testing SLD function...")
    a_star(map, sld, g)


