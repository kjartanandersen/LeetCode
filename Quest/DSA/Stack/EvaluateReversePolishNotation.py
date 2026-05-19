from typing import List, Callable

class Input:
    def __init__(self, target: List[str]):
        self.target = target

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        validOperators = ["+", "-", "*", "/"]
        numStack = []

        for token in tokens:
            
            if token in validOperators:
                
                rightVal = numStack.pop()
                leftVal = numStack.pop()
                newVal = 0

                if token == "+":
                    newVal = int(leftVal) + int(rightVal) 
                if token == "-":
                    newVal = int(leftVal) - int(rightVal) 
                if token == "/":
                    newVal = int(int(leftVal) / int(rightVal)) 
                if token == "*":
                    newVal = int(leftVal) * int(rightVal) 
                numStack.append(newVal)
                
            else:
                numStack.append(token)
                
            
            
        
        return int(numStack.pop())
        

        

def testListStrToInt(tokens: List[str], func) -> int:
    print("Input: "  + tokens.__str__())
    print("Output: " + str(func(tokens)))




if __name__ == "__main__":
    sol = Solution()



    inps: List[Input] = []
    inps.append(Input(["2","1","+","3","*"]))
    inps.append(Input(["4","13","5","/","+"]))
    inps.append(Input(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

    for inp in inps:
        testListStrToInt(inp.target, sol.evalRPN)
        print("")


    