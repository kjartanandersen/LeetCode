from typing import List, Callable

class Input:
    def __init__(self, target: List[int], n: int):
        self.target = target
        self.n = n

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetLen = len(target)

        PushPopStack = []
        s = [0] * targetLen
        isFinished = False
        i = 0
        nInc = 1

        while not isFinished:
            s[i] = nInc
            PushPopStack.append("Push")

            isNumFinished = False
            while not isNumFinished:
                if s[i] != target[i]:
                    PushPopStack.append("Pop")
                    PushPopStack.append("Push")
                    nInc += 1
                    s[i] = nInc
                else:
                    isNumFinished = True
            
            if s[targetLen-1] == target[targetLen-1]:
                isFinished = True
            
            i += 1
            nInc += 1


            

        return PushPopStack
        

        

def testListIntToInt(input: List[int], n: int, func):
    print("Input: "  + input.__str__() + ", " + str(n))
    print("Output: " + str(func(input, n)))


if __name__ == "__main__":
    sol = Solution()



    inps: List[Input] = []
    inps.append(Input([1,3], 3))
    inps.append(Input([1,2,3], 3))
    inps.append(Input([1,2], 4))

    for inp in inps:
        testListIntToInt(inp.target, inp.n, sol.buildArray)
        print("")


    