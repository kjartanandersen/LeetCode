from typing import List
from collections import Counter

class Solution:
    def removeStars(self, s: str) -> str:
        
        strStack = []

        for i in s:
            if i == '*':
                strStack.pop()
            else:
                strStack += [i]

        

        return "".join(strStack)

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.removeStars( s = "leet**cod*e" )))
    

    