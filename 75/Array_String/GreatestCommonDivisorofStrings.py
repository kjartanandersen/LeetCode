
from typing import List

class Solution:

    def gcd(self, a: int, b: int):
        return b if a == 0 else self.gcd(b % a, a)

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[:self.gcd(len(str1), len(str2))]
        



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.gcdOfStrings( str1 = "ABCABC", str2 = "ABC" )))