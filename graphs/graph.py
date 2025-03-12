from collections import deque

class Graph:

    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.add_node(u)
        if v not in self.adj_list:
            self.add_node(v)

        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def display(self):
        for node, neighbours in self.adj_list.items():
            print(f'{node} --> {neighbours}')

    def dfs(self, node, visited = None):
        if visited == None:
            visited = {}

        visited[node] = True
        print(node)

        for neighbour in self.adj_list.get(node, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def bfs(self, node):
        visited = {node : True}
        Q = deque([node])

        while Q:
            current_node = Q.popleft()
            print(current_node)
            for neighbour in self.adj_list.get(current_node, []):
                if neighbour not in visited:
                    visited[neighbour] = True
                    Q.append(neighbour)

def main():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)

    print("Graph Representation:")
    graph.display()

    print('DFS:')
    graph.dfs(1)

    print('BFS')
    graph.bfs(1)

if __name__ == '__main__':
    main()
