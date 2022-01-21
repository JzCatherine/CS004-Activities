# addEdge() Function is used to append the edges in the adjacent list
def addEdge(graph, node1, node2, weight):
    graph[node1].append([node2, weight])
    graph[node2].append([node1, weight])
    return graph

# dijkstra() function performs the Dijkstra's algorithm that 
# finds the shortest path from a given starting node 
# to every other node in the graph
def dijkstra(graph, source):
    # distance list stores the shortest paths from the starting node and every other node in the graph
    distance = [[None for c in range(2)] for r in range(len(graph))]
    # visited list keeps track of the vertices that are visited
    visited = []
    # unvisited list vertices that the program haven't visited yet
    unvisited = list(range(0, len(graph)))
    # Initialize the source node. Distance to the source from source = 0
    distance[source][0] = 0
    # Initialize the current distance as 0, it represents the distance to source from source
    currentDistance = 0
    
    #The loop runs while all the nodes have been visited
    while True:
        # For loop runs visits all the nodes until the parent loop is satisfied (all the nodes have been visited)
        for node in range(len(graph)):
            # if the current node is not in the unvisited the loop will immediately jump to the next iteration/node
            if node not in unvisited: continue
            
            # This for loop visits the unvisited node with the smallest known distance from the source node
            # initialize shortpath to boolean value false. Will be used to check if the current node has the shortest known distance from the source
            shortpath = False
            # initialize the value of min to a highest value. Will be used to track the value of the node with the shortest known distance from the source
            min = 9999
            for i in range(len(distance)):
                if i not in unvisited: continue
                # if the value of the shortest known distance from the source of the current node is not none and less than the min value
                # then the minimum value will be replaced by the current shortest known distance found in the distance list
                if distance[i][0] is not None and distance[i][0] < min:
                    min = distance[i][0]
                    # if the current node in the distance list matched with the node from the parent loop, then the value shortpath is replaced with True
                    if i == node:
                        shortpath = True
                    else:
                        shortpath = False

            # If the shortpath is false then the current node does not have the smallest known distance from the source node and the loop will immediately jump to the next iteration/node
            if shortpath is not True:
                continue
            
            # If the current node is found to have the smallest known distance from the source node the program will examine its unvisited neighbours
            # for loop will visit the neighbours of the current node
            currentDistance = distance[node][0]
            for neighbour in range(len(graph[node])):
                # calculate the distance of the current neighbour from the start node
                newDistance = currentDistance + graph[node][neighbour][1]
                # if the calculated new distance is less than the known distance , update the shortest distance and previous node in distance list
                if distance[graph[node][neighbour][0]][0] is None or distance[graph[node][neighbour][0]][0] > newDistance:
                    distance[graph[node][neighbour][0]][0] = newDistance
                    distance[graph[node][neighbour][0]][1:] = distance[node][1:]
                    distance[graph[node][neighbour][0]].append(node)
           
            # append current node to the visited list and remove it from the unvisited list
            unvisited.remove(node)
            visited.append(node)
            
        # Once the unvisited list is empty the while loop will stop
        if not unvisited: break
    # return distance    
    return distance    

# display function displays the result, which is the shortest path from the given starting node to every other node in the graph
def display(distance, source):
    source = source
    print('=' * 90)
    print(" Node", f"\t\tShortest distance from {source}", "\tLeast-cost Path")
    print('-' * 90)
    for i in range(len(distance)):
        print(" ", i, '\t'*2, "{}".format(distance[i][0]), '\t'*4, end="")
        print(*(distance[i][2:]), i, sep = ' -> ')
    print('=' * 90)


# Driver Code of the Program
print('=' * 90, "\n\t\t\tD I J K S T R A 'S   A L G O R I T H M")
print('=' * 90)
vertices = int(input(" Enter the number of nodes in the graph: "))
source = int(input(" Enter the source node: "))
edges = int(input(" Enter the number of edges in the graph: "))
print('-' * 90)

# Create a adjacency list representation of the weighted graph
graph = [[] for i in range(vertices)]
# Gets the user input for the edges of the weighted graph
x = range(edges)
for n in x:
    print(f" Edge #{n+1}")
    node1 = int(input("\tEnter Node: "))
    node2 = int(input("\tEnter Node: "))
    weight = int(input(f"\tEnter Weight between node {node1} & node {node2}: "))
    graph = addEdge(graph, node1, node2, weight)


# sample given 1
#   no. of nodes = 5
#   source node = 0
#   no. of edges = 7
# graph = addEdge(graph, 0, 1, 10)
# graph = addEdge(graph, 0, 4, 20)
# graph = addEdge(graph, 1, 2, 30)
# graph = addEdge(graph, 1, 3, 40)
# graph = addEdge(graph, 1, 4, 50)
# graph = addEdge(graph, 2, 3, 60)
# graph = addEdge(graph, 3, 4, 70)

# sample given 2
#   no. of nodes = 5
#   source node = 0
#   no. of edges = 7
# graph = addEdge(graph, 0, 1, 6)
# graph = addEdge(graph, 0, 3, 1)
# graph = addEdge(graph, 1, 2, 5)
# graph = addEdge(graph, 1, 3, 2)
# graph = addEdge(graph, 1, 4, 2)
# graph = addEdge(graph, 2, 4, 5)
# graph = addEdge(graph, 3, 4, 1)

# sample given 3
#   no. of nodes = 9
#   source node = 0
#   no. of edges = 14
# graph = addEdge(graph, 0, 1, 4)
# graph = addEdge(graph, 0, 7, 8)
# graph = addEdge(graph, 1, 2, 8)
# graph = addEdge(graph, 1, 7, 11)
# graph = addEdge(graph, 2, 3, 7)
# graph = addEdge(graph, 2, 8, 2)
# graph = addEdge(graph, 2, 5, 4)
# graph = addEdge(graph, 3, 4, 9)
# graph = addEdge(graph, 3, 5, 14)
# graph = addEdge(graph, 4, 5, 10)
# graph = addEdge(graph, 5, 6, 2)
# graph = addEdge(graph, 6, 7, 1)
# graph = addEdge(graph, 6, 8, 6)
# graph = addEdge(graph, 7, 8, 7)


distance = dijkstra(graph, source)
display(distance, source)

