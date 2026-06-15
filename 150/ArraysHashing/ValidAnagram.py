from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
            
        return True

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.isAnagram( s = "racecar", t = "carrace" )))
    print(str(solution.isAnagram( s = "jar", t = "jam" )))
    

    