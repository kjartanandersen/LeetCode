from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        sumAllNums = (1+len(nums)) * len(nums) // 2
        sumUniq = sum(set(nums))
        sumNums = sum(nums)

        dup = sumNums - sumUniq
        miss = sumAllNums - sumUniq

        return [dup, miss]
        
    
        
if __name__ == "__main__":
    sol = Solution()
    list = sol.findErrorNums([1,2,2,4])
    print(list)