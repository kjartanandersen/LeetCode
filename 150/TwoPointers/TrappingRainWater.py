

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        leftPtr = 0
        rightPtr = len(height) - 1
        maxLeft = height[leftPtr]
        maxRight = height[rightPtr]
        retVal = 0

        while leftPtr < rightPtr:
            if maxLeft < maxRight:
                leftPtr += 1
                maxLeft = max(maxLeft, height[leftPtr])
                retVal += maxLeft - height[leftPtr]
            else:
                rightPtr -= 1
                maxRight = max(maxRight, height[rightPtr])
                retVal += maxRight - height[rightPtr]
        
        return retVal
    
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.trap( height = [0,2,0,3,1,0,1,3,2,1] )))

    