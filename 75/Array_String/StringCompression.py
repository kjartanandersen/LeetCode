
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        readPtr = 0
        writePtr = 0
        arrLen = len(chars)

        while readPtr < arrLen:
            
            currentChar = chars[readPtr]
            count = 0

            while readPtr < arrLen and chars[readPtr] == currentChar:
                count += 1
                readPtr += 1

            chars[writePtr] = currentChar
            writePtr += 1

            if count > 1:
                for digit in str(count):
                    chars[writePtr] = digit
                    writePtr += 1

        return writePtr
                
                
                



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.compress(  ["a","a","b","b","c","c","c"]  )))