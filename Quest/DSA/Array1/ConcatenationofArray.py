from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums) * 2

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]

        return ans
        



if __name__ == "__main__":
    solution = Solution()

    print(solution.getConcatenation([1,3,5]))
    pass