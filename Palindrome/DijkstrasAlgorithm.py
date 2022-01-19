class Solution:
    def dijkstrasAlgorithm(self,start, edges):
        numNodes = len(edges)
        visited  =set()
        minDistances = [float('inf') for _ in range(numNodes)]
        minDistances[start] = 0

        while(len(visited)!=numNodes):
            vertex, currentMinDistance = self.relaxVertices(minDistances,visited)
            
            if currentMinDistance==float('inf'):
                break

            visited.add(vertex)
            for edge in edges[vertex]:
                v,distToDest = edge
                if(v in visited):
                    continue
                newpathDistance = currentMinDistance + distToDest
                if newpathDistance < minDistances[v]:
                    minDistances[v] = newpathDistance
        return list(map(lambda x: -1 if x==float('inf') else x,minDistances))

    def relaxVertices(self,distances,visited):
        currentMinDistance = float('inf')
        vertex = -1
        for vertexIdx,distance in enumerate(distances):
            if vertexIdx in visited:
                continue
            if(distance<=currentMinDistance):
                vertex = vertexIdx
                currentMinDistance = distance
        return vertex, currentMinDistance

if __name__=='__main__':
    start = 0
    edges = [
    [
      [1, 7]
    ],
    [
      [2, 6],
      [3, 20],
      [4, 3]
    ],
    [
      [3, 14]
    ],
    [
      [4, 2]
    ],
    [],
    []
    ]
    s = Solution()
    print(s.dijkstrasAlgorithm(start,edges))