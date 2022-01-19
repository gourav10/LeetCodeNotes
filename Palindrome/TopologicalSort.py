from platform import node


class Node:
    def __init__(self,job) -> None:
        self.prereqs = list()
        self.job = job
        self.visited = False
        self.visiting  = False

class JobGraph:
    def __init__(self,jobs) -> None:
        self.jobs = list()
        self.graph = dict()
        for i in jobs:
            self.addNode(i)
        

    def addNode(self,job):
        self.graph[job] = Node(job)
        self.jobs.append(self.graph[job])
    
    def getNode(self,job):
        if(job in self.graph):
            return self.graph[job]
        return self.addNode(job)

    def addPrereqs(self,prereq,job):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

class Solution:
    def topologicalSort(self,jobs,deps):
        #Step 1: Generate the graph
        graph = self.createJobGraph(jobs,deps)
        return self.orderedJobList(graph)
    
    def createJobGraph(self,jobs,deps):
        graph = JobGraph(jobs)
        for prereq,job in deps:
            graph.addPrereqs(prereq,job)
        return graph

    def orderedJobList(self,graph):
        result = []
        nodes = graph.jobs
        while(len(nodes)):
            node = nodes.pop()
            hasCycles = self.checkCycles(node,result)
            if(hasCycles):
                return []
        return result

    def checkCycles(self,node,result):
        if(node.visited):
            return False
        if(node.visiting):
            return True
        node.visiting = True
        for prereq in node.prereqs:
            hasCycle = self.checkCycles(prereq,result)
            if(hasCycle):
                return True
        node.visited = True
        node.visiting = False
        result.append(node.job)
        return False
    
if __name__=='__main__':
    jobs = [1,2,3,4]
    deps = [[1,2],[1,3],[3,2],[4,2],[4,3]]
    s = Solution()
    result = s.topologicalSort(jobs,deps)
    print(result)
