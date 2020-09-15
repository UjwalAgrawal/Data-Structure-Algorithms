# Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges
# (Many DAGs have more than just one topological ordering. You may output any of them.)

from collections import defaultdict

class graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, p,q):
        self.adj[p].append(q)
    
    def dfs(self, ver):
        self.visited = defaultdict(bool)
        self.stack=[]
        for i in range(1,ver+1):
            if(self.visited[i]==False):
                self._dfs(i)
        return(self.stack)
    
    def _dfs(self, u):
        self.visited[u] = True
        for i in self.adj[u]:
            if(self.visited[i]==False):
                self._dfs(i)
        self.stack.insert(0,u)

if __name__ == "__main__":
    ver,e = map(int, input().split())
    g = graph()
    for i in range(e):
        u,v = map(int,input().split())
        g.addEdge(u,v)    
    print(*g.dfs(ver))