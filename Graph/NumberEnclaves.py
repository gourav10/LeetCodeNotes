from typing import List

class Solution:
    def __init__(self):
        self.visited = None
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.visited = [[False for col in row] for row in grid]
        landCounter = 0
        #Perform DFS on the borders
        for i in range(len(grid[0])):
            if(grid[0][i]!=1):
                continue
            self.dfs(grid,0,i)
        
        for i in range(len(grid)):
            if(grid[i][0]!=1):
                continue
            self.dfs(grid,i,0)
        
        lastColIdx = len(grid[0])-1
        for i in range(len(grid)):
            if(grid[i][lastColIdx]!=1):
                continue
            self.dfs(grid,0,len(grid)-1)
            
        lastRowIdx = len(grid) -1
        
        for i in range(len(grid[lastRowIdx])):
            if(grid[i][lastColIdx]!=1):
                continue
            self.dfs(grid,lastRowIdx,i)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]==1):
                    landCounter+=1
        
        return landCounter
    
    def dfs(self,grid,i,j):
        frontier = [(i,j)]
        while(frontier):
            i,j = frontier.pop()
            if(self.visited[i][j]):
                continue
                
            if(grid[i][j]==0):
                continue
            self.visited[i][j]= True
            grid[i][j]+=1
            #neighbours = self.getNeighbours(grid,i,j)
            for x,y in [(-1,0),(0,-1),(+1,0),(0,+1)]:
                frontier.append((i+x,j+y))
        print(grid)
    
    def getNeighbours(self,grid,i,j):
        neighbours=[]
        if(i>0 and not self.visited[i-1][j]):
            neighbours.append((i-1,j))
        if(i>0 and not self.visited[i][j-1]):
            neighbours.append((i,j-1))    
        if(i>0 and not self.visited[i+1][j]):
            neighbours.append((i+1,j))
        if(i>0 and not self.visited[i][j+1]):
            neighbours.append((i,j+1))
        return neighbours


if __name__=='__main__':
    grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
    grid2 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    s = Solution()
    result = s.numEnclaves(grid)
    print(result)