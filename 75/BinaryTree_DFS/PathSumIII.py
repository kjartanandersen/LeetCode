from typing import Counter, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        counter = Counter({0: 1})

        def pathSumDFS(node: Optional[TreeNode], s: int) -> int:
            if node is None:
                return 0
            
            s += node.val
            ans = counter[s - targetSum]
            counter[s] += 1

            ans += pathSumDFS(node.left, s)
            ans += pathSumDFS(node.right, s)

            counter[s] -= 1

            return ans

        return pathSumDFS(root, 0)

if __name__ == "__main__":

    solution = Solution()
    root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))

    print(solution.pathSum( root=root, targetSum=8 ))

    
