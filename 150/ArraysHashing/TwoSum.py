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

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.twoSum( nums = [3,4,5,6], target = 7 )))
    print(str(solution.twoSum( nums = [4,5,6], target = 10 )))
    

    