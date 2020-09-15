# Task: Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and
# 𝑚 edges.

from collections import defaultdict
import sys
sys.setrecursionlimit(200000) #overriding the default limit

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.rev_adj = defaultdict(list)
    
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.rev_adj[v].append(u)
    
    def dfs(self, V):
        self.stack=[]
        self.visited = defaultdict(bool)
        self.visited_rev = defaultdict(bool)
        c=0
        for i in range(1,V+1):
            if(self.visited[i]==False):
                self._dfs(i)
        
        while(self.stack):
            i = self.stack.pop()
            if(self.visited_rev[i]==False):
                self._dfs_for_scc(i)
                c+=1
        return(c)

    #making of stack
    def _dfs(self, u):
        self.visited[u] = True
        for i in self.adj[u]:
            if(self.visited[i]==False):
                self._dfs(i)
        self.stack.append(u)
    
    def _dfs_for_scc(self,s):
        self.visited_rev[s] = True
        for i in self.rev_adj[s]:
            if(self.visited_rev[i]==False):
                self._dfs_for_scc(i)


if __name__ == "__main__":
    g= Graph()
    ver, edges = map(int, input().split())
    for _ in range(edges):
        u,v = map(int, input().split())
        g.addEdge(u,v)
    print(g.dfs(ver))