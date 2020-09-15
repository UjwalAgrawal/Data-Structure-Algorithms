# Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle

from collections import defaultdict

class graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, p,q):
        self.adj[p].append(q)
    
    def dfs(self,ver):
        self.visited = defaultdict(bool)
        self.rec = defaultdict(bool)
        for i in range(1, ver+1):
            if(self.visited[i]==False):
                if(self._dfs(i)):
                    return(1)
        return(0)
    
    def _dfs(self, u):
        self.visited[u] = True
        self.rec[u] = True
        for i in self.adj[u]:
            if(self.visited[i]==False):
                if(self._dfs(i)):
                    return(True)
            elif(self.rec[i]):
                return(True)
        self.rec[u] = False
        return(False)


if __name__ == "__main__":
    ver,e = map(int, input().split())
    g = graph()
    for i in range(e):
        u,v = map(int,input().split())
        g.addEdge(u,v)    
    print(g.dfs(ver)) #pass random vertex and examine acyclicity