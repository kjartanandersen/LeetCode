

from typing import List

class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()

        lptr = 0
        rptr = len(nums) - 1
        eqKCount = 0

        while lptr < rptr:
            if nums[lptr] + nums[rptr] == k:
                eqKCount += 1
                lptr += 1
                rptr -= 1
            elif nums[lptr] + nums[rptr] > k:
                rptr -= 1
            elif nums[lptr] + nums[rptr] < k:
                lptr += 1
        
        return eqKCount


if __name__ == "__main__":

    solution = Solution()
    print(str(solution.maxOperations( nums = [3,1,3,4,3], k = 6 )))

    