
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        paranDict = {}
        paranDict[')'] = '('
        paranDict[']'] = '['
        paranDict['}'] = '{'

        paranStack = []

        for n, c in enumerate(s, 0):
            if c in '([{':
                paranStack.append(c)
            else:
                if len(paranStack) != 0:
                    cmpParan = paranStack.pop()
                    if not cmpParan == paranDict.get(c, '#'):
                        return False
                else:
                    return False

        if len(paranStack) != 0:
            return False    
        return True
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.isValid( s = "[]" )))
    print(str(solution.isValid( s = "([{}])" )))

    print(str(solution.isValid( s = "[(])" )))
    print(str(solution.isValid( s = "((" )))
    print(str(solution.isValid( s = "]]" )))
    
    
    

    