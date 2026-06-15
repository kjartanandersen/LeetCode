from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ListToTreeNode(list: List[int]) -> TreeNode:

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        outArr = []

        q = deque([root])

        while q:
            rs = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rs = node
                    q.append(node.left)
                    q.append(node.right)

            if rs:
                outArr.append(rs.val)
                
        return outArr


if __name__ == "__main__":

    solution = Solution()
    root = ListToTreeNode([1,2,3,None,5,None,4])

    print(solution.rightSideView( root ))
    # print()

    
    
    

    
