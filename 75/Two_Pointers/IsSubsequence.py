

from typing import List

class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        tLen = len(t)
        sLen = len(s)
        amntCorr = 0
        i = 0

        while amntCorr != sLen and i < tLen:
            if t[i] == s[amntCorr]:
                amntCorr += 1
                if amntCorr == sLen:
                    return True
                
            i += 1

        return False


if __name__ == "__main__":

    solution = Solution()
    print(str(solution.isSubsequence( s = "", t = "" )))

    