
from typing import List

#
# [1, 2, 4, 6]
#
# [ 1,  2,  8, 48]
# [48, 48, 24,  6]
#

#
# [-1, 0, 1, 2, 3]
#
# [-1, 0, 0, 0, 0 ]
# [ 0, 0, 6, 6, 3 ]
#



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res



if __name__ == "__main__":

    solution = Solution()

    input = [-1, 0, 1, 2, 3]

    output = solution.productExceptSelf(input)

    print(str(output))