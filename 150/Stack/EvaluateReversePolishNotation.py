
from typing import List
from math import trunc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        tokenStack = []

        for t in tokens:
            if   t == '+':
                rightT = tokenStack.pop()
                leftT = tokenStack.pop()

                tokenStack.append(int(leftT) + int(rightT))
            elif t == '-':
                rightT = tokenStack.pop()
                leftT = tokenStack.pop()

                tokenStack.append(int(leftT) - int(rightT))
            elif t == '*':
                rightT = tokenStack.pop()
                leftT = tokenStack.pop()

                tokenStack.append(int(leftT) * int(rightT))
            elif t == '/':
                rightT = tokenStack.pop()
                leftT = tokenStack.pop()

                tokenStack.append(trunc(int(leftT) / int(rightT)))
            else:
                tokenStack.append(int(t))

        return int(tokenStack.pop())
if __name__ == "__main__":

    solution = Solution()
    print(solution.evalRPN( tokens = ["1","2","+","3","*","4","-"] ))
    print(solution.evalRPN( tokens = ["1", "3", "+", "5", "/"] ))
    print(solution.evalRPN( tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"] ))
    print(solution.evalRPN( tokens=["18"] ))
    
    
    

    