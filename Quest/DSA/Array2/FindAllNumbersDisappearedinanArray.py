from typing import List

# [ 1, 1, 2, 3, 4 ]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        
        numSet = set(nums)

        return [x for x in range(1, len(nums) + 1) if x not in numSet]

        
        
if __name__ == "__main__":
    sol = Solution()
    list = sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print(list)