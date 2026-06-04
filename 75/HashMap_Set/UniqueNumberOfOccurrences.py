from typing import List

class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:

        elemFreq = {}
        for num in arr:
            elemFreq[num] = elemFreq.get(num, 0) + 1

        return len(elemFreq) == len(set(elemFreq.values()))

        
        '''
        arrDict = {}
        
        if len(arr) == 1:
            return True
        
        for num in arr:
            if arrDict.get(num):
                arrDict[num] += 1
            else:
                arrDict[num] = 1

        arrDict = dict(sorted(arrDict.items(), key=lambda item: item[1]))

        idx = 0
        prevVal = 0
        for v in arrDict:
            if idx >= 1:
                if arrDict.get(v) == prevVal:
                    return False
                
            prevVal = arrDict.get(v)
            idx += 1
        
        return True
            
        '''


    
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.uniqueOccurrences( arr = [1, 2] )))
    

    