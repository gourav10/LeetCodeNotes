from operator import truediv


class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.neighbours = []
        self.visiting = False
        self.visited = False

class JobGraph:
    def __init__(self,edges) -> None:
        self.nodes = list()
        self.graph = dict()
        for i in range(len(edges)):
            self.addNode(i)
    
    def addEdge(self,nodeVal, neighbourVal):
        node = self.getNode(nodeVal)
        neighbourNode = self.getNode(neighbourVal)
        node.neighbours.append(neighbourNode)

    def getNode(self,nodeVal):
        if(nodeVal not in self.graph):
            self.addNode(nodeVal)
        return self.graph[nodeVal]
        
    def addNode(self,nodeVal):
        node = Node(nodeVal)
        self.graph[nodeVal] = node
        self.nodes.append(self.graph[nodeVal])

class Solution:
    def cycleInGraph(self,edges):
        graph = self.generateGraph(edges)
        return self.detectCycles(graph)
    
    def generateGraph(self,edges):
        graph = JobGraph(edges)
        for i,edge in enumerate(edges):
            for v in edge:
                graph.addEdge(i,v)
        return graph


    def detectCycles(self,graph):
        nodes = graph.nodes
        while(len(nodes)):
            root = nodes.pop()
            hasCycle = self.dfs(root)
            if(hasCycle):
                return True
        return False

    def dfs(self,root):
        if(root.visited):
            return False
        if(root.visiting):
            return True
        root.visiting = True
        for v in root.neighbours:
            hasCycle = self.dfs(v)
            if(hasCycle):
                return True
        root.visited = True
        root.visiting  = False 
        return False

if __name__=="__main__":
    s = Solution()
    edges = [[1, 2],[2],[1]]
    print(s.cycleInGraph(edges))