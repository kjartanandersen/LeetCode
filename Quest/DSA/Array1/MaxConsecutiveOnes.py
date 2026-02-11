from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxOneCount = 0
        currOneCount = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                currOneCount += 1
            else:
                currOneCount = 0

            if currOneCount > maxOneCount:
                    maxOneCount = currOneCount
        return maxOneCount

if __name__ == "__main__":
    solution = Solution()

    print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
    