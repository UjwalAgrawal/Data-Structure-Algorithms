# Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components in it.
# Input Format. A graph is given in the standard format.

from collections import defaultdict
from random import choice

class graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, p,q):
        self.adj[p].append(q)
        self.adj[q].append(p)
    
    def dfs(self, ver):
        self.visited = defaultdict(bool)
        self.listy = list(range(1, ver+1))
        c = 0
        while(self.listy):
            u = choice(self.listy)
            c+=1
            self._dfs(u)
        return(c)
    
    def _dfs(self, u):
        self.visited[u] = True
        self.listy.remove(u)
        for i in self.adj[u]:
            if(self.visited[i]==False):
                self._dfs(i)

if __name__ == "__main__":
    ver,e = map(int, input().split())
    g = graph()
    for i in range(e):
        u,v = map(int,input().split())
        g.addEdge(u,v)    
    print(g.dfs(ver))