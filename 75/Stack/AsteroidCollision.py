from typing import List
from collections import Counter

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.asteroidCollision( asteroids = [3,5,-6,2,-1,4] )))
    

    