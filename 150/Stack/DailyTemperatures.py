
from typing import List
from math import trunc


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        retVal = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackI = stack.pop()
                retVal[stackI] = (i - stackI)
            stack.append([t, i])

        return retVal

if __name__ == "__main__":

    solution = Solution()
    print(solution.dailyTemperatures( temperatures = [30,38,30,36,35,40,28] ))
    print(solution.dailyTemperatures( temperatures = [22,21,20] ))

    
    
    

    