from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            
            currMinTmp = currMin * n
            currMaxTmp = currMax * n
            currMax = max(currMaxTmp, currMinTmp, n)
            currMin = min(currMaxTmp, currMinTmp, n)
            res = max(res, currMax)

        return res

        
        
if __name__ == "__main__":
    sol = Solution()
    list = sol.maxProduct([2,3,-2,4])
    print(list)
