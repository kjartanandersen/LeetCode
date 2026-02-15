from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # [ 1, 2, 2, 3, 8 ]
        sortArr = nums.copy()
        sortArr.sort()
        numsCount = {}


        for i in range(len(nums)-1, 0, -1):
            if sortArr[i-1] < sortArr[i]:
                numsCount[sortArr[i]] = i
            if i == 1:
                numsCount[sortArr[i-1]] = 0

        for i in range(len(nums)):
            nums[i] = numsCount[nums[i]]

        return nums
        # countArr = [0] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
# 
        #         if nums[i] > nums[j]:
        #             countArr[i] += 1
# 
        # return countArr
        
        
    
        
if __name__ == "__main__":
    sol = Solution()
    list = sol.smallerNumbersThanCurrent([8,1,2,2,3])
    print(list)