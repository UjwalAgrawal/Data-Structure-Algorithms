from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, v):
        self.visited = defaultdict(bool)
        self._dfs(v)

    def _dfs(self, v):
        self.visited[v]= True
        print(v, end=" ")
        for i in self.graph[v]:
            if(self.visited[i]==False):
                self._dfs(i)


if __name__ == "__main__":
    myGraph = Graph()
    ver,e = map(int, input().split()) #Number of vertices and edges
    for i in range(e):
        u,v = input().split()
        myGraph.addEdge(u,v)
    p=input() #starting point for DFS
    myGraph.DFS(p)