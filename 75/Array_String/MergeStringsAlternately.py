
from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1Len = len(word1)
        w2len = len(word2)

        mergedWord = []

        i = 0
        while i < w1Len or i < w2len:
            if (i < w1Len):
                mergedWord.append(word1[i])
            if (i < w2len):
                mergedWord.append(word2[i])
            i += 1

        return ''.join(mergedWord)



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.mergeAlternately( word1 = "abc", word2 = "pqr" )))