from typing import List
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:


        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        if set(count1.keys()) != set(count2.keys()):
            return False

        return sorted(count1.values()) == sorted(count2.values())

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.closeStrings( word1 = "abc", word2 = "bca" )))
    

    