from tkinter import SOLID


class Solution:
    def minimumPassesOfMatrix(self,matrix):
        passes = self.convertMatrixToPositive(matrix)
        return passes - 1 if not self.containsNegative(matrix) else -1

    def convertMatrixToPositive(self,matrix):
        nextPassQueue = self.getAllPositiveNums(matrix)
        passes = 0
        while(len(nextPassQueue)>0):
            currentQueue = nextPassQueue
            nextPassQueue = []

            while(len(currentQueue)>0):
                currentRow, currentCol = currentQueue.pop(0)
                neighbours = self.getNeighbours(currentRow,currentCol, matrix)
                for neighbour in neighbours:
                    x,y = neighbour
                    value = matrix[x][y]
                    if(value<0):
                        value = value*-1
                        nextPassQueue.append([x,y])
            passes+=1
        return passes
    
    def getAllPositiveNums(self,matrix):
        positiveNums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]>0):
                    positiveNums.append([i,j])
        return positiveNums
    
    def getNeighbours(self,row,col, matrix):
        neighbours = []
        if(row>0):
            neighbours.append([row-1,col])
        if(row<len(matrix)-1):
            neighbours.append([row+1,col])
        if(col>0):
            neighbours.append([row,col-1])
        if(col<len(matrix[row])):
            neighbours.append([row,col+1])
        return neighbours

    def containsNegative(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]<0):
                    return True
        return False

if __name__=='__main__':
    matrix = [[0,-2,-1],[-5,2,0],[-6,-2,0]]
    s= Solution()
    print(s.minimumPassesOfMatrix(matrix))