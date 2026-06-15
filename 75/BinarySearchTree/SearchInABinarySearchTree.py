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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:

            if not root.left and root.left:
                return None
            

            if root.val == val:
                return root

            
            if root.left:

                left = dfs(root.left)
                if left:
                    if left.val == val:
                        return left
            
            if root.right:
                right = dfs(root.right)
                if right:

                    if right.val == val:
                        return right
            

        return dfs(root)

if __name__ == "__main__":

    solution = Solution()
    root = ListToTreeNode( [4,2,7,1,3] )

    sol = solution.searchBST( root, 2 )
    print()
    print()

    
    
    

    
