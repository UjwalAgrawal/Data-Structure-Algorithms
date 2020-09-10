# Task: Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
# Input Format: An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
# and 𝑣 of the graph.

from collections import defaultdict

class graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, p,q):
        self.adj[p].append(q)
        self.adj[q].append(p)
    
    def dfs(self, u,v):
        self.visited = defaultdict(bool)
        self.listy = []
        self._dfs(u)
        return(q in self.listy)
        
    def _dfs(self, u):
        self.visited[u] = True
        self.listy.append(u)
        for i in self.adj[u]:
            if(self.visited[i]==False):
                self._dfs(i)


if __name__ == "__main__":
    ver,e = map(int, input().split())
    g = graph()
    for i in range(e):
        u,v = input().split()
        g.addEdge(u,v)    
    p, q = input().split()
    print(g.dfs(p,q))
    