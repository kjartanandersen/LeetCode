

from typing import List

class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:


        left = 0
        zeroCount = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeroCount += 1

            if zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1

                left += 1

        return len(nums) - left

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.longestOnes( nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 )))
    

    