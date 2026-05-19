from typing import List, Callable

class Input:
    def __init__(self,n: int, target: List[str]):
        self.n = n
        self.target = target

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        answer = [0] * n
        pre = 0

        for log in logs:
            logSpl = log.split(':')
            id = int(logSpl[0])
            op = logSpl[1]
            cur = int(logSpl[2])

            if (op[0] == "s"):
                if stack:
                    answer[stack[-1]] += cur - pre
                
                stack.append(id)
                pre = cur
            
            else:
                endFunc = stack.pop()
                answer[endFunc] += cur - pre + 1

                pre = cur + 1


        return answer
        
        

        

def test_NInt_ListStr_To_ListInt(n: int, tokens: List[str], func) -> List[int]:
    print("Input: "  + tokens.__str__())
    print("Output: " + str(func(n, tokens)))




if __name__ == "__main__":
    sol = Solution()



    inps: List[Input] = []
    inps.append(Input(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    inps.append(Input(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    inps.append(Input(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))

    for inp in inps:
        test_NInt_ListStr_To_ListInt(inp.n, inp.target, sol.exclusiveTime)
        print("")


    