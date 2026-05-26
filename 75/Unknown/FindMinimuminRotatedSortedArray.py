from typing import List, Callable

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if (nums[m] >= nums[l]):
                l = m + 1
            else:
                r = m - 1

        return res

        

def testListToInt(input: List[int], func):
    print("Input: "  + input.__str__())
    print("Output: " + str(func(input)))


if __name__ == "__main__":
    sol = Solution()

    inps = []
    inps.append([3,4,5,1,2])
    inps.append([4,5,6,7,0,1,2])
    inps.append([11,13,15,17])

    for inp in inps:
        testListToInt(inp, sol.findMin)
        print("")


    