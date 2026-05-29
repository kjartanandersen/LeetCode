from typing import List

class Solution:

    def largestAltitude(self, gain: List[int]) -> int:


        currPoint = 0
        maxPoint = 0

        for i in range(len(gain)):

            currPoint += gain[i]
            maxPoint = max(maxPoint, currPoint)

        return maxPoint


if __name__ == "__main__":

    solution = Solution()
    print(str(solution.largestAltitude( gain = [-4,-3,-2,-1,4,3,2] )))
    

    