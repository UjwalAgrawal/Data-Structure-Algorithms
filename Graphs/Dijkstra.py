# Given an directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two
# vertices 𝑢 and 𝑣, compute the weight of a shortest path between 𝑢 and 𝑣 (that is, the minimum total
# weight of a path from 𝑢 to 𝑣).
# Output the minimum weight of a path from 𝑢 to 𝑣, or −1 if there is no path

from collections import defaultdict
import heapdict

class Graph:
    def __init__(self):
        self.adj  = defaultdict(list)
        self.w = {}
        self.visited = defaultdict(bool)
    
    def addEdge(self, u,v, w):
        self.adj[u].append(v)
        self.w[(u,v)] = w   #edge cost
    
    def dijkstra(self, u,v):
        #setting the length so high that any value at first would come lesser than it
        #distance is infinite unless traversed
        self.dist = defaultdict(lambda:1000000000)
        self.dist[u] = 0 #distance of self node is always 0 in non-negative graph
        #using heap of type dictionary that returns tuple of least priority
        q = heapdict.heapdict() 
        q[u]=0 #distance from itself is 0
        while(q.__len__()):
            i = q.popitem()[0]
            if self.visited[i] == False:
                for node in self.adj[i]:
                    if(self.dist[node]>self.dist[i]+self.w[i,node]):
                        self.dist[node]=self.dist[i]+self.w[i,node]
                        q[node]=self.dist[node]
        
        return(self.dist[v]) if(self.dist[v]!=1000000000) else -1
    


if __name__ == "__main__":
    vertex, edges = map(int, input().split())
    g = Graph()
    for _ in range(edges):
        u,v,w = map(int, input().split())
        g.addEdge(u,v,w)
    p, q = map(int, input().split())    #nodes between which shortest distance is to found
    print(g.dijkstra(p,q))