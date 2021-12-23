from typing import DefaultDict


class Graph:
    def __init__(self,V) -> None:
        self.V = V
        self.graph = DefaultDict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def FindMother(self):
        visited = set()
        v=0
        for i in range(self.V):
            if i in visited:
                continue
            self.DFSUtil(visited,i)
            v = i

        visited = set()
        self.DFSUtil(visited,v)
        for i in range(self.V):
            if(i in visited): continue
            else: return -1
        return v

    def DFSUtil(self,visited,v):
        visited.add(v)
        for i in self.graph[v]:
            if i in visited: continue
            self.DFSUtil(visited,i)

if __name__=="__main__":
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    print("A mother vertex is " + str(g.FindMother()))
