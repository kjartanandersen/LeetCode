

from typing import List

class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if n == k:
            totalSum = 0.0

            for i in range(n):
                totalSum += nums[i]
            return totalSum / k
        
        maxSum = 0.0
        for i in range(k):
            maxSum += nums[i]
        currentSum = maxSum
        for i in range(k, n):
            currentSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, currentSum)
        return maxSum / k

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.findMaxAverage( nums = [1,12,-5,-6,50,3], k = 4 )))
    print(str(solution.findMaxAverage( nums = [5], k = 1 )))
    print(str(solution.findMaxAverage( nums = [0,1,1,3,3], k = 4 )))

    