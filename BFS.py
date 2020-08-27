from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, start):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(start)
        visited[start] = True
        while(queue):
            q = queue.pop(0)
            print(q, end=" ")
            for i in self.graph[q]:
                if(visited[i]==False):
                    queue.append(i)
                    visited[i]=True

myGraph = Graph()
myGraph.addEdge(0,1)
myGraph.addEdge(0,2)
myGraph.addEdge(0,3)
myGraph.addEdge(1,2)
myGraph.addEdge(2,3)
myGraph.addEdge(3,3)
myGraph.BFS(2)
