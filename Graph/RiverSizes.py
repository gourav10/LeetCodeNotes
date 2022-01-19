class Solution:

    def riverSizes(self,matrix):
        visited = [[False for col in row] for row in matrix]
        riverSize = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(visited[i][j]):
                    continue
                self.dfs(matrix,i,j,visited,riverSize)
        riverSize.sort()
        return riverSize
        
    
    def dfs(self,matrix,row,col,visited,riverSize):
        frontier =[(row,col)]
        river=0
        while(len(frontier)!=0):
            x,y = frontier.pop()
            if(visited[x][y]):
                continue
            visited[x][y]=True
            if(matrix[x][y]==0):
                continue
            river+=1
            
            neighbours = self.getNeighbours(x,y,matrix,visited)
            for neighbour in neighbours:
                i,j = neighbour
                frontier.append((i,j))

        if(river>0):
            riverSize.append(river)
        return riverSize

    def getNeighbours(self,row,col,matrix,visited):
        neighbours = []
        if(row>0 and not visited[row-1][col]):
            neighbours.append((row-1,col))
        if(row<len(matrix)-1 and not visited[row+1][col]):
            neighbours.append((row+1,col))
        if(col>0 and not visited[row][col-1]):
            neighbours.append((row,col-1))
        if(col<len(matrix[row])-1 and not visited[row][col+1]):
            neighbours.append((row,col+1))
        return neighbours



if __name__=='__main__':
    matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
    ]
    s = Solution()
    print(s.riverSizes(matrix))