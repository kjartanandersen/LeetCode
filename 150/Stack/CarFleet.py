
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        
if __name__ == "__main__":

    solution = Solution()
    print(solution.carFleet( target = 10, position = [1,4], speed = [3,2] ))
    print(solution.carFleet( target = 10, position = [4,1,0,7], speed = [2,2,1,1] ))

    
    
    

    