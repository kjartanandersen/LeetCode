
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        leftPtr = 0
        rightPtr = len(numbers)-1

        while leftPtr < rightPtr:
            currSum = numbers[leftPtr] + numbers[rightPtr]

            if currSum < target:
                leftPtr += 1
            elif currSum > target:
                rightPtr -= 1
            else:
                return [leftPtr+1, rightPtr+1]

        return []
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.twoSum( numbers = [1,2,3,4], target = 3 )))
    print(str(solution.twoSum( numbers = [2,6,7,11,15,17,20], target = 18 )))
    
    

    