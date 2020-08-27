from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, v):
        self.visited = [False]*(max(self.graph)+1)
        self._dfs(v)

    def _dfs(self, v):
        self.visited[v]= True
        print(v, end=" ")
        for i in self.graph[v]:
            if(self.visited[i]==False):
                self._dfs(i)



myGraph = Graph()
myGraph.addEdge(0,1)
myGraph.addEdge(0,2)
myGraph.addEdge(0,3)
myGraph.addEdge(1,2)
myGraph.addEdge(2,3)
myGraph.addEdge(3,3)
myGraph.DFS(0)