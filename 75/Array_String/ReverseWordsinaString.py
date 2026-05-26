
from typing import List

class Solution:

    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        revWords = words[::-1]
        return ' '.join(revWords)



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.reverseWords( s = "the sky is blue" )))