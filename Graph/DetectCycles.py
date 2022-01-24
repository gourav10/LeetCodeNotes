class Node:
    def __init__(self,val) -> None:
        self.value = val
        self.neighbours = []
        self.visited = False
        self.visiting = False

class JobGraph:
    def __init__(self,edges) -> None:
        self.vertices = []
        self.graph = dict()
        for v in range(len(edges)):
            self.addNode(v)
    
    def addNode(self,nodeVal):
        node = Node(nodeVal)
        self.graph[nodeVal] = node

    def getNode(self,nodeVal):
        if(nodeVal not in self.graph):
            self.addNode(nodeVal)
        return self.graph[nodeVal]

    def addEdge(self,u,v):
        node1 = self.getNode(u)
        node2 = self.getNode(v)
        node1.append(node2)
        self.graph[u] = node1

class Solution:
    def cycleInGraph(self,edges):
        graph = self.generateGraph(edges)
        return self.cycleCheck(graph)

    def generateGraph(self,edges):
        graph = JobGraph(edges)
        for u in range(len(graph)):
            for v in range(len(graph[u])):
                graph.addEdge(u,v)
        return graph
    
    def cycleCheck(self,graph):
        nodes = graph.vertices
        while(len(nodes)>0):
            u = nodes.pop()
            hasCycle = self.dfs(u)
            if(hasCycle):
                return False
        return True

    def dfs(self,root):
        if(root.visited):
            return False
        if(root.visiting):
            return True
        root.visiting = True
        for v in root.neighbours:
            hasCycle = self.dfs(v)
            if(hasCycle):
                return False
        root.visited = True
        root.visiting = False
        return False
