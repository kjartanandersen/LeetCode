

from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:

        lptr = 0
        rptr = len(height) - 1

        mArea = 0

        while lptr != rptr:
            
            currArea = min(height[lptr], height[rptr]) * (rptr - lptr)
            if currArea > mArea:
                mArea = currArea

            if height[lptr] < height[rptr]:
                lptr += 1
            
            else:
                rptr -= 1

        return mArea

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.maxArea( height = [1,1] )))

    