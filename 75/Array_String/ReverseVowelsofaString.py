
from typing import List

class Solution:

    def reverseVowels(self, s: str) -> str:
        
        l = 0
        r = len(s) - 1

        vowels = set("aeiouAEIOU")
        revVowString = list(s)

        while l < r:

            if s[l] in vowels and s[r] in vowels:
                revVowString[l] = s[r]
                revVowString[r] = s[l]
                l += 1
                r -= 1

            elif l < r and s[r] not in vowels:
                r -= 1

            elif l < r and s[r] in vowels:
                l += 1

            
        return ''.join(revVowString)
        



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.reverseVowels( s = "IceCreAm" )))