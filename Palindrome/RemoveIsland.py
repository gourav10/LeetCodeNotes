def removeIslands(matrix):
    visited = [[False for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rowBorder = i==0 or i==len(matrix)-1
            columnBorder = j==0 or j==len(matrix[i])-1
            isBorder = rowBorder or columnBorder
            if(not isBorder or matrix[i][j]!=1):
                continue
            dfs(matrix,i,j,visited)
	
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]==1):
                matrix[i][j]=0
            elif(matrix[i][j]>1):
                matrix[i][j]=1

    return matrix

def dfs(matrix,i,j,visited):
	frontier = [(i,j)]
	while(frontier):
		x,y = frontier.pop()
		visited[x][y]=True
		matrix[x][y]=2
		neighbours = getNeighbours(matrix,x,y)
		for neighbour in neighbours:
			row,col = neighbour
			if(matrix[row][col]!=1):
				continue
			frontier.append(neighbour)

def getNeighbours(matrix,row,col):
	neighbours=[]
	
	totRows = len(matrix)
	totCols = len(matrix[row])
	
	if(row-1>=0):
		neighbours.append((row-1,col))
	if(row+1<totRows):
		neighbours.append((row+1,col))
	if(col-1>=0):
		neighbours.append((row,col-1))
	if(col+1<totCols):
		neighbours.append((row,col+1))
	return neighbours

if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
    print(removeIslands(matrix))