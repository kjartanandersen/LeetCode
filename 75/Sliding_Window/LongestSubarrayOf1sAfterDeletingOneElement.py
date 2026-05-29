from typing import List

class Solution:

    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        right = 0
        zeroCount = 0
        maxLength = 0

        while right < len(nums):

            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxLength = max(maxLength, right - left)
            right += 1

        return maxLength

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.longestSubarray( nums = [1,1,0,1] )))
    

    