from typing import DefaultDict

class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = DefaultDict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

class Solution:
    def BFS(self,graph, start):
        
        adjList = DefaultDict(list)
        for item in graph:
            adjList[item[0]].append(item[1])
        print(adjList)   

        frontier = []
        visited = set()

        frontier.append(start)
        
        visited.add(start)
        result = ""
        while(len(frontier)!=0):
            u = frontier.pop(0)
            result+= str(u)+" "
            
            visited.add(u)

            for v in adjList[u]:
                if(v in visited):
                    continue
                visited.add(v)
                frontier.append(v)

        print(result)

        


        



if __name__=="__main__":
    graph = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
    s = Solution()
    s.BFS(graph,2)

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFS(2)



