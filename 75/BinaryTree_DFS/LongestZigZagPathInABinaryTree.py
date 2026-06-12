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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.maxLen = 0

        def dfs(node: Optional[TreeNode], direction: str,  length: int):
            if not node:
                return
            
            self.maxLen = max(self.maxLen, length)

            if direction == 'left':
                dfs(node.left, 'left', 1)
                dfs(node.right, 'right', length+1)
            else:
                dfs(node.left, 'left', length+1)
                dfs(node.right, 'right', 1)

        dfs(root.left, 'left', 1)
        dfs(root.right, 'right', 1)

        return self.maxLen


if __name__ == "__main__":

    solution = Solution()
    
    root = ListToTreeNode([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])

    print(solution.longestZigZag( root ))
    
    root = ListToTreeNode([1,1,1,None,1,None,None,1,1,None,1])

    print(solution.longestZigZag( root ))

    root = ListToTreeNode([1])

    print(solution.longestZigZag( root ))
    
    
    

    
