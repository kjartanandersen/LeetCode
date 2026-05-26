

from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        leadZeroPos = 0
        it = 0
        n = len(nums)
        while it < n:
            if nums[it] != 0:
                nums[leadZeroPos] = nums[it]
                leadZeroPos += 1
            it += 1
        for i in range(leadZeroPos, n):
            nums[i] = 0

            



if __name__ == "__main__":

    solution = Solution()

    nums = [0,1,0,3,12]
    print(f"Before: {nums}")
    solution.moveZeroes(nums)
    print(f"After: {nums}")

    