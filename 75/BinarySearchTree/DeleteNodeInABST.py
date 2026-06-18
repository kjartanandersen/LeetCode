from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ListToTreeNode(list: List[int]) -> Optional[TreeNode]:

    if not list:
        return None

    root = TreeNode(list[0])
    queue = [root]
    i = 1

    while queue and i < len(list):
        node = queue.pop(0)

        if list[i] is not None:
            node.left = TreeNode(list[i])
            queue.append(node.left)
        i += 1

        if i < len(list) and list[i] is not None:
            node.right = TreeNode(list[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getSuccessor(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            curr = curr.right

            while curr and curr.left:
                curr = curr.left

            return curr
        
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            succ = getSuccessor(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

        return root
        

if __name__ == "__main__":

    solution = Solution()
    root = ListToTreeNode( [5,3,6,2,4,None,7] )

    sol = solution.deleteNode( root, 3 )
    print()
    print()

    
    
    

    
