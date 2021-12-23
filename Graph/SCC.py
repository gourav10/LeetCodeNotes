#Strongly Connected Components
##
# Algorithm:
# 1) Use DFS to find the nodes with highest finish time and store in stack.
# 2) Reverse the direction of all edges in graph
# 3) One by one pop item from stack and store the connected vertices in set
# ##

class Solution:
    def computeSCC(self,graph):
        visited = set()
        itemStack = []
        for u in graph:
            if(u in visited):continue
            self.DFS(graph, u, itemStack, visited)

        altGraph = self.reverseEdges(graph)
        result = self.DFS_ReverseGraph(altGraph,itemStack,visited)
        return result

    def DFS(self,graph,u,itemStack,visited):
        visited.add(u)
        for v in graph[u]:
            if(v in visited): continue
            self.DFS(graph,u,itemStack,visited)
        itemStack = itemStack.append(v)
    
    def reverseEdge(self,graph):
        pass

    def DFS_ReverseGraph(graph,itemStack,visited):
        pass

