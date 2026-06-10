from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafList(root) -> List[int]:

            retArr = []

            nodeStack = [root]

            while nodeStack:
                evalNode = nodeStack.pop()

                if not evalNode.left and not evalNode.right:
                    retArr.append(evalNode.val)
                else:
                    if evalNode.left:
                        nodeStack.append(evalNode.left)
                    if evalNode.right:
                        nodeStack.append(evalNode.right)

            return retArr    
        

        root1List = getLeafList(root1)
        root2List = getLeafList(root2)

        return root1List == root2List

        


if __name__ == "__main__":

    solution = Solution()
    root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))

    print(solution.leafSimilar( root1, root2 ))
    print()

    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(3), TreeNode(2))

    print(solution.leafSimilar( root1, root2 ))
    
    

    
