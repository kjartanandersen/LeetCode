from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodeDFS(TNode: TreeNode, maxVal: int) -> int:
            if not TNode:
                return 0
            
            retVal = 1 if TNode.val >= maxVal else 0
            maxVal = max(maxVal, TNode.val)
            retVal += goodNodeDFS(TNode.left, maxVal)
            retVal += goodNodeDFS(TNode.right, maxVal)
            return retVal
        
        return goodNodeDFS(root, root.val)


if __name__ == "__main__":

    solution = Solution()
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))

    print(solution.goodNodes( root ))
    # print()

    
    
    

    
