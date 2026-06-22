
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        i = 0
        retArr = []

        while i < len(nums)-1:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            leftPtr = i+1
            rightPtr = len(nums)-1

            while leftPtr < rightPtr:
                target = -nums[i]
                if (nums[leftPtr] + nums[rightPtr]) < target:
                    leftPtr += 1
                elif (nums[leftPtr] + nums[rightPtr]) > target:
                    rightPtr -= 1
                else:
                    retArr.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    while nums[leftPtr] == nums[leftPtr-1] and leftPtr < rightPtr:
                        leftPtr += 1
            
            i += 1

        return retArr
    
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.threeSum( nums = [-1,0,1,2,-1,-4] )))
    print(str(solution.threeSum( nums = [0,1,1] )))
    print(str(solution.threeSum( nums = [0,0,0] )))
    print(str(solution.threeSum( nums = [0,0,0, 0] )))
    
    

    