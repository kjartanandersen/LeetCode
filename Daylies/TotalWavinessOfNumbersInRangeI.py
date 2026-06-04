from typing import List
from collections import Counter

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def count_waviness(num: int) -> int:
            s = str(num)
            if len(s) < 3:
                return 0
            
            waviness = 0
            for i in range(1, len(s) - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    waviness += 1
            
            return waviness
        total_waviness = 0
        for num in range(num1, num2 + 1):
            total_waviness += count_waviness(num)
        return total_waviness
    

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.totalWaviness( num1 = 120, num2 = 130 )))
    

    