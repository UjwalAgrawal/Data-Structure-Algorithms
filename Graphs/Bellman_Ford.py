from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = []
        self.vertices = set()

    def addEdge(self, u, v, w) -> None:
        self.graph.append([u, v, w])
        self.vertices.add(u)
        self.vertices.add(v)

    def bellman_ford(self, source) -> None:
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[source] = 0

        for _ in range(len(self.vertices)-1):
            for u, v, w in self.graph:
                if (self.dist[v] > self.dist[u] + w and self.dist[u] != float('inf')):
                    self.dist[v] = self.dist[u] + w

    def printAllDistances(self) -> None:
        for key in self.dist:
            print(f"{key} : {self.dist[key]}")


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1, 10)
    g.addEdge(0, 5, 8)
    g.addEdge(1, 3, 2)
    g.addEdge(2, 1, 1)
    g.addEdge(3, 2, -1)
    g.addEdge(4, 1, -4)
    g.addEdge(4, 3, -1)
    g.addEdge(5, 4, 1)

    g.bellman_ford(0)
    g.printAllDistances()
