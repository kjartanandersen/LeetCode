

from typing import List

class Solution:

    def maxVowels(self, s: str, k: int) -> int:

        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(s)
        idx = 0
        currMaxVow = 0

        while idx < k:
            if s[idx] in vowels:
                currMaxVow += 1
            idx += 1

        if k == n:
            return currMaxVow
        
        totalMaxVow = currMaxVow

        for i in range(0, n - k):

            if s[i] in vowels:
                currMaxVow -= 1
            if s[i + k] in vowels:
                currMaxVow += 1

            totalMaxVow = max(totalMaxVow, currMaxVow)
            
        return totalMaxVow

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.maxVowels( s = "abciiidef", k = 3 )))
    

    