# Breadth First Search algorithm for connected graphs

from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source_vertex, destination_vertex):
        self.graph[source_vertex].append(destination_vertex)

    def breath_first_search(self, source):
        queue = []
        visited_vertices = [False] * (max(self.graph) + 1)

        queue.append(source)
        visited_vertices[source] = True

        while queue:
            vertex = queue.pop(0)

            print(vertex, end=" ")

            for i in self.graph[vertex]:
                if not visited_vertices[i]:
                    queue.append(i);
                    visited_vertices[i] = True


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

graph.breath_first_search(2)
