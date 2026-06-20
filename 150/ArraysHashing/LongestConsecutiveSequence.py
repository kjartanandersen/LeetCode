from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(NlogN) solution
        #
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return 1
        # 
        # nums.sort()
        # 
        # currConsecSeqLen = 1
        # maxConsecSeqLen = 0
        # prevNum = nums[0]
        # 
        # for i in range(1, len(nums)):
        #     if nums[i] == prevNum:
        #         continue
        #     if nums[i] == prevNum+1:
        #         currConsecSeqLen += 1
        #     else:
        #         maxConsecSeqLen = max(maxConsecSeqLen, currConsecSeqLen)
        #         currConsecSeqLen = 1
        #     prevNum = nums[i]
        # 
        # return max(maxConsecSeqLen, currConsecSeqLen)

        #O(n) solution
        numSet = set(nums)
        currConsecSeqLen = 0
        maxConsecSeqLen = 0

        for n in nums:
            if (n - 1) not in numSet:
                currConsecSeqLen = 0
                while (n + currConsecSeqLen) in numSet:
                    currConsecSeqLen += 1
                maxConsecSeqLen = max(maxConsecSeqLen, currConsecSeqLen)

        return maxConsecSeqLen
        
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.longestConsecutive( nums = [2,20,4,10,3,4,5]         )))
    print(str(solution.longestConsecutive( nums = [0,3,2,5,4,6,1,1]         )))
    print(str(solution.longestConsecutive( nums = [9,1,4,7,3,-1,0,5,8,-1,6] )))
    

    