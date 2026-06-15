from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return False
        
        nums.sort()

        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]:
                return True
            
        return False

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.hasDuplicate( nums = [1, 2, 3, 3] )))
    print(str(solution.hasDuplicate( nums = [1, 2, 3, 4] )))
    

    