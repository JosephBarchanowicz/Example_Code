from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def display(self):
        return self.adjacency_list

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("Vertex Exists in Graph")
        self.adjacency_list[vertex] = []
        return self

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid verticies")
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid verticies")
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("Vertex Exists in Graph")
        for neighbor in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor].remove(vertex)
        self.adjacency_list.pop(vertex)
        return self

    def breadth_first_traversal(self, start):
        if start in self.adjacency_list:
            raise Exception("Vertex Exists in Graph")
        queue = deque()
        queue.append(start)
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}
        explored[start] = True
        while queue:
            current = queue.popleft()
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    queue.append(adjacent)
                    explored[adjacent] = True

    def dft_iterative(self, start):
        if start in self.adjacency_list:
            raise Exception("Vertex Exists in Graph")
        stack = [start]
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}
        explored[start] = True
        while stack:
            current = stack.pop()
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    stack.append(adjacent)
                    explored[adjacent] = True
        return visited

    def dft_recursive(self, start):
        if start in self.adjacency_list:
            raise Exception("Vertex Exists in Graph")
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}

        def _traverse(current):
            visited.append(current)
            explored[current] = True
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    _traverse(adjacent)

        _traverse(start)
        return visited




g = Graph()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
print(g.display())
g.add_edge("a", "b")
g.add_edge("a", "c")
print(g.display())
