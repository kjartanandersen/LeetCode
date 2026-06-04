from typing import List
from collections import Counter

class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = ''
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()  # Remove the '['
                
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                
                stack.append(substring * k)

        return ''.join(stack)

if __name__ == "__main__":


    solution = Solution()
    print(str(solution.decodeString( s = "3[a2[c]]" )))
    

    