import routefinder
from mars_planner import RoverState, action_list, mission_complete
from search_algorithms import *
from antennae import antennae_main


if __name__=="__main__" :

    # Question 2
    print("testing DFS...")
    s = RoverState()
    result = depth_first_search(s, action_list, mission_complete)
    print(result)
    print("------------------")
    print("testing BFS...")
    s = RoverState()
    result = breadth_first_search(s, action_list, mission_complete)
    print(result)
    print("------------------")
    print("testing DLS...")
    s = RoverState()
    result = depth_first_search(s, action_list, mission_complete, True, 7)
    print(result)

    # Question 2, part 6:

    # BFS:
    print("------------------")
    print("BFS problem decomposition...")
    state = RoverState()
    def g(state):
        return state.loc == "sample"
    print("moving to sample...")
    result = breadth_first_search(state, action_list, g)
    print(result)
    def g2(state):
        return state.sample_extracted == True
    print("removing sample...")
    result = breadth_first_search(state, action_list, g2)
    print(result)
    def g3(state):
        return state.loc == "battery"
    print("returning to charger...")
    result = breadth_first_search(state, action_list, g3)
    print(result)
    print("------------------")

    # DFS:
    print("DFS problem decomposition...")
    state = RoverState()
    def g(state):
        return state.loc == "sample"
    print("moving to sample...")
    result = depth_first_search(state, action_list, g)
    print(result)
    def g2(state):
        return state.sample_extracted == True
    print("removing sample...")
    result = depth_first_search(state, action_list, g2)
    print(result)
    def g3(state):
        return state.loc == "battery"
    print("returning to charger...")
    result = depth_first_search(state, action_list, g3)
    print(result)
    print("------------------")

    # Question 3
    print("testing routefinder...")
    routefinder.main()

    print("------------------")

    print("printing antennae...")
    antennae_main()



