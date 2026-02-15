from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numSet = set()
        for n in nums:
            
            if n in numSet:
                return True
            numSet.add(n)

        return False
        
        
if __name__ == "__main__":
    sol = Solution()
    list = sol.containsDuplicate([1,2,3,4])
    print(list)
