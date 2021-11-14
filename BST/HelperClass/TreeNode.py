from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, val =0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self,root = None) -> List[int]:
        #Level Order traversal
        temp = root
        frontier = Queue()
        while(root!=None):
            if root.left!=None:
                frontier.append
            