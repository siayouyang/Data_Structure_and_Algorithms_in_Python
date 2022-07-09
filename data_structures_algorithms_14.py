#14 graph algorithms(BFS, DFS, shortest path)
#weighted, directed graphs

#normal graph
num_nodes1 = 5
edges1 = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

# weighed graph
num_nodes2 = 9
edges2 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]
print(num_nodes2,len(edges2))

# directed graph
num_nodes3 = 5
edges3 = [(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)]
print(num_nodes3,len(edges3))

# weighted-directed graph
num_nodes4 = 6
edges4 = [(0,1,4),(0,2,2),(1,2,5),(1,3,10),(2,4,3),(4,3,4),(3,5,11)]
print(num_nodes4,len(edges4))

class Graph:
    def __init__(self, num_nodes, edges, weighted=False, directed=False):
        self.num_nodes = num_nodes
        self.edges = edges
        self.weighted = weighted
        self.directed = directed
        self.adjacency_list = [[] for _ in range(num_nodes)]
        self.weight_list = [[] for _ in range(num_nodes)]
        if self.weighted is True:
            for i, j, weight in self.edges:
                self.adjacency_list[i].append(j)
                self.weight_list[i].append(weight)
                if self.directed is False:
                    self.adjacency_list[j].append(i)
                    self.weight_list[j].append(weight)
        elif self.weighted is False:
            for i, j in self.edges:
                self.adjacency_list[i].append(j)
                if self.directed is False:
                    self.adjacency_list[j].append(i)

    def __repr__(self):
        if self.weighted is True:
            zip_list = []
            for n in range(len(self.adjacency_list)):
                zip_list.append(list(zip(self.adjacency_list[n],self.weight_list[n])))
            represent = '\n'.join(['{} : {}'.format(idx, lst) for idx, lst in enumerate(zip_list)])
        else:
            represent = '\n'.join(['{} : {}'.format(idx, lst) for idx, lst in enumerate(self.adjacency_list)])

        return f'{represent}'

    def __str__(self):
        return self.__repr__()


graph1 = Graph(num_nodes1, edges1)
print('normal\n', graph1)
graph2 = Graph(num_nodes2, edges2, weighted=True)
print('weighted\n',graph2)
graph3 = Graph(num_nodes3, edges3, directed=True)
print('directed\n', graph3)
graph4 = Graph(num_nodes4, edges4, directed=True, weighted=True)
print('weighted-directed\n', graph4)


#shortest paths
#Dijkstra's algorithm


def update_distance(graph, current_node, node_distance, parent_list):
    for idx, node in enumerate(graph.adjacency_list[current_node]):
        new_distance = node_distance[current_node] + graph.weight_list[current_node][idx]
        if new_distance < node_distance[node]:
            node_distance[node] = new_distance
            parent_list[node] = current_node


def pick_next_node(node_distance, visited_list):
    min_distance = float('inf')
    for node, distance in enumerate(node_distance):
        if distance < min_distance and visited_list[node] == False:
            min_distance = distance
            min_node = node
    visited_list[min_node] = True
    return min_node

def shortest_path(graph, source, target):
    if target > graph.num_nodes-1 :
        return f"target exceeds range"
    node_distance = [float('inf') for _ in range(graph.num_nodes)]
    visited_list = [False for _ in range(graph.num_nodes)]
    parent_list = [None for _ in range(graph.num_nodes)]
    current_node = source
    node_distance[current_node] = 0
    visited_list[current_node] = True
    while current_node != target:
        update_distance(graph, current_node, node_distance, parent_list)
        current_node = pick_next_node(node_distance, visited_list)

    route = [target]
    n = target
    while n is not None:
        route.append(parent_list[n])
        n = parent_list[n]

    return node_distance[current_node], parent_list, list(reversed(route))

print(shortest_path(graph4, source=0, target=5))
print(shortest_path(graph2, source=0, target=7))
print(shortest_path(graph4, source=0, target=6))


