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

# my_dict.get('apple', 0) + 1  
# max_key = max(my_dict, key=my_dict.get)
# print(max_key)  # 

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        sumMap = dict()

        def dfs(root: Optional[TreeNode], level: int):
            
            if not root:
                return

            sumMap[level] = sumMap.get(level, 0) + root.val

            if root.left:
                dfs(root.left,  level+1)
            if root.right:
                dfs(root.right, level+1)

        dfs(root, 1)

        return max(sumMap, key=sumMap.get)


if __name__ == "__main__":

    solution = Solution()

    root = ListToTreeNode( [1,7,0,7,8,None,None] )
    print(solution.maxLevelSum( root ))
    print()

    root = ListToTreeNode( [989,None,10250,98693,-89388,None,None,None,-32127] )
    print(solution.maxLevelSum( root ))
    
    
    
    

    
