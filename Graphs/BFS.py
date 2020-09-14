from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, start):
        visited = defaultdict(bool)
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

if __name__ == "__main__":
    myGraph = Graph()
    ver,e = map(int, input().split()) #Number of vertices and edges
    for i in range(e):
        u,v = input().split()
        myGraph.addEdge(u,v)
    p=input() #starting point for DFS
    myGraph.BFS(p)


