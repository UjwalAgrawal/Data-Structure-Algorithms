# Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle

from collections import defaultdict

class graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, p,q):
        self.adj[p].append(q)
    
    def dfs(self,u):
        self.visited = defaultdict(bool)
        self.f = 0  #flag
        self._dfs(u)
        return(1) if self.f else 0
    
    def _dfs(self, u):
        self.visited[u] = True
        for i in self.adj[u]:
            if(self.visited[i]==False):
                self._dfs(i)
            else:
                self.f = 1

if __name__ == "__main__":
    ver,e = map(int, input().split())
    g = graph()
    for i in range(e):
        u,v = map(int,input().split())
        g.addEdge(u,v)    
    print(g.dfs(u)) #pass random vertex and examine acyclicity