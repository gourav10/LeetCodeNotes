from typing import Counter


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

class Solution:
    def getYoungestCommonAncestor(self,topAncestor, descendantOne, descendantTwo):
        h1 = self.getHeight(descendantOne, topAncestor)
        h2 = self.getHeight(descendantTwo, topAncestor)
        if(h2>h1):
            diff = h2 - h1
            
            while(diff>0):
                descendantTwo=descendantTwo.ancestor
                diff-=1
            
            
        elif(h1>h2):
            diff = h1-h2
            while(diff>0):
                descendantOne=descendantOne.ancestor
                diff-=1


        commonAncestor = self.getCommonAncestor(topAncestor, descendantOne, descendantTwo)

        return commonAncestor

    def getCommonAncestor(self, topAncestor, descendantOne, descendantTwo):
        while(descendantOne!=descendantTwo):
            descendantTwo = descendantTwo.ancestor
            descendantOne = descendantOne.ancestor
        return descendantOne

            

    def getHeight(self,node,topAncestor):
        height = 0
        while(node!=topAncestor):
            height+=1
            node = node.ancestor
        return height
        
if __name__=='__main__':
    s = Solution()
    nodeA = AncestralTree('A')
    nodeB = AncestralTree('B')
    nodeB.ancestor = nodeA
    nodeC = AncestralTree('C')
    nodeC.ancestor = nodeA

    nodeD = AncestralTree('D')
    nodeD.ancestor = nodeB
    nodeE = AncestralTree('E')
    nodeE.ancestor = nodeB

    nodeF = AncestralTree('F')
    nodeF.ancestor = nodeC
    nodeG = AncestralTree('G')
    nodeG.ancestor = nodeC

    nodeH = AncestralTree('H')
    nodeH.ancestor = nodeD
    nodeI = AncestralTree('I')
    nodeI.ancestor = nodeD

    print(s.getYoungestCommonAncestor(nodeA,nodeE,nodeI).name)
