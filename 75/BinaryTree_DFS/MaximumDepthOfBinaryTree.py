from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:
            return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


if __name__ == "__main__":

    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    print(solution.maxDepth(root))
    print()
    
    root = TreeNode(1, None, TreeNode(2))
    print(solution.maxDepth(root))
    
