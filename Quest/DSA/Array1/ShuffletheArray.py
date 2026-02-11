from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        if (len(nums) // 2 != n):
            return []

        
        ans = [0] * len(nums)
        lenn = len(nums)
        for i in range(0, len(nums), 2):
            ans[i] = nums[i//2]
            ans[i+1] = nums[i//2+n]

        return ans



if __name__ == "__main__":
    solution = Solution()

    print(solution.shuffle([2,5,1,3,4,7], 3))
    