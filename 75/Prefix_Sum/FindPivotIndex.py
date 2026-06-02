from typing import List

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        rsum = sum(nums)
        idx = 0
        n = len(nums)

        if n == 1:
            return 0

        while idx < n:
            rsum -= nums[idx]
            if lsum == rsum:
                return idx
            
            lsum += nums[idx]

            idx += 1

        return -1

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.pivotIndex( nums = [2,1,-1] )))
    

    