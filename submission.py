from routefinder import read_mars_graph, sld, a_star

if __name__=="__main__" :


    ## route finder:

    graph = read_mars_graph("MarsMap")

    a_star(graph)


