import math
from os.path import split
from queue import PriorityQueue

from Graph import Graph, Edge, Node
from mars_planner import RoverState, action_list, mission_complete


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = read_mars_graph(mars_graph)
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
    print("search queue: ", search_queue.queue)
    mars_graph = start_state.mars_graph

    # if use_closed_list:
    closed_list[start_state] = True
    while search_queue.qsize() > 0 :
        next_state = search_queue.get()
        print("next state: ", next_state[1])
        if goal_test(next_state[1]):
            print("Goal found")
            print(next_state[1])
            ptr = next_state[1]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state[1]
        else :
            edges = mars_graph.get_edges(next_state[1].location)
            # print("edges: ", edges)
            # print("edges: ", str(edges[0]).split())
            for e in edges :
                g = next_state[1].g
                h = sld(e.dest)
                m = map_state(location=e.dest, mars_graph="MarsMap", prev_state=next_state[1], g=g, h=h)
                f = g + h
                if m not in closed_list :
                    search_queue.put((f, m))
            # print("e: ", e)
            # search_queue.put((sld(e), e))
            # print("search queue after adding: ", search_queue.queue)

    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    print("state: ", state)
    coordinates = state.split(",")
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
                # print("e: ", e)
                graph.add_edge(e)

    return graph

def g(s):
    print("s: ", s)
    return s.location == "1,1"

if __name__=="__main__" :
    map = map_state(location="8,8", mars_graph="MarsMap")
    a_star(map, sld, g)


