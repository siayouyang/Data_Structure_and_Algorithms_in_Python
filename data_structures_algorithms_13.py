#13 graph algorithms(BFS, DFS, shortest path)

num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
print(num_nodes, len(edges))

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.adjacency_list = [[] for _ in range(self.num_nodes)]
        for i, j in self.edges:
            self.adjacency_list[i].append(j)
            self.adjacency_list[j].append(i)

    def add_edge(self, edge):
        i, j = edge
        if edge not in self.edges and i < self.num_nodes and j < self.num_nodes:
            self.edges.append(edge)
            self.adjacency_list[i].append(j)
            self.adjacency_list[j].append(i)

    def remove_edge(self, edge):
        i, j = edge
        if edge in self.edges:
            self.edges.remove(edge)
            self.adjacency_list[i].remove(j)
            self.adjacency_list[j].remove(i)

    def __repr__(self):
        repr = '\n'.join(['{} : {}'.format(idx, lst) for idx, lst in enumerate(self.adjacency_list)])
        return f'{repr}'

    def __str__(self):
        return self.__repr__()

graph1 = Graph(num_nodes, edges)
print(graph1)
graph1.add_edge((0,3))
print('\n', graph1, graph1.edges)
graph1.add_edge((0,4))  #will not be added
print('\n', graph1, graph1.edges)
graph1.remove_edge((0,3))
print('\n', graph1, graph1.edges)

#Breadth-First Search
def bfs(graph, root):
    data = graph.adjacency_list
    discovered = [False for _ in range(graph.num_nodes)]
    distance = [0 for _ in range(graph.num_nodes)]
    parent = [None for _ in range(graph.num_nodes)]

    queue = [root]
    discovered[root] = True

    idx = 0
    while idx < len(queue):
        q = queue[idx]     #first in first out
        for lst in data[q]:
            if discovered[lst] is False:
                queue.append(lst)
                distance[lst] = 1 + distance[q]
                parent[lst] = q
                discovered[lst] = True
        idx += 1

    return queue, distance, parent

print(bfs(graph1, 3))

#Depth-First Search
def dfs(graph, root):
    data = graph.adjacency_list
    discovered = [False for _ in range(graph.num_nodes)]
    result = []
    stack = [root]
    discovered[root] = True

    while len(stack) > 0:
        q = stack.pop()  # last in first out
        result.append(q)
        for lst in data[q]:
            if discovered[lst] is False:
                stack.append(lst)
                discovered[lst] = True#

    return result

print(dfs(graph1, 3))

#Depth-First Search
def dfs_v2(graph, root):
    data = graph.adjacency_list
    discovered = [False for _ in range(graph.num_nodes)]
    result = []
    stack = [root]

    while len(stack) > 0:
        q = stack.pop()  # last in first out
        if discovered[q] is False:
            discovered[q] = True
            result.append(q)
            for lst in data[q]:
                if discovered[lst] is False:
                    stack.append(lst)


    return result

print(dfs_v2(graph1, 3))