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
    
class Solution2:
    waves = []
    for i in range(1000):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10
        if (m > max(l, r)) | (m < min(l, r)):
            waves.append(i)

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.waveCount(num2) - self.waveCount(num1 - 1)

    def waveCount(self, num):
        if num < 100: return 0
        return sum(self.countWays(num, p) for p in self.waves)

    def countWays(self, num, pattern):
        s = str(num)
        n = len(s)
        t = pattern < 100
        count = 0
        for i in range(n - 2):
            pre = int(s[:i] or 0)
            cur = int(s[i:i+3])
            suf = int(s[i+3:] or 0)
            mult = 10 ** (n - i - 3)
            ways = 0

            if cur > pattern:
                ways = pre - t + 1
            elif cur == pattern:
                ways = max(0, pre - t)
                count += suf + 1                
            else:
                ways = max(0, pre - t)
            count += ways * mult

        return count

if __name__ == "__main__":

    solution = Solution2()
    print(str(solution.totalWaviness( num1 = 4848, num2 = 4848 )))
    

    