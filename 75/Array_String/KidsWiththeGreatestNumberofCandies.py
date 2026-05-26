
from typing import List

class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandy = 0

        result = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] > maxCandy:
                maxCandy = candies[i]

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxCandy:
                result[i] = True

        return result



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.kidsWithCandies( candies = [4,2,1,1,2], extraCandies = 1 )))