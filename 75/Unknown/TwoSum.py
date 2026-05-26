from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = dict()

        for i in range(len(nums)):
            
            for j in range(len(numMap)):
                
                if numMap[j] == target - nums[i]:
                    return [j, i]

            numMap[i] = nums[i]

        return []
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        numMap = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numMap:
                return [numMap[diff], i]
            numMap[n] = i
        
        return 




if __name__ == "__main__":
    sol = Solution()
    list = sol.twoSum2([2, 7, 11, 15], 26)
    print(list)