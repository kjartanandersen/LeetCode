from typing import List

class Solution:


    
    def encode(self, strs: List[str]) -> str:

        encodedString = ""
        for s in strs:
            
            encodedString += str(len(s))  + "#" + s

        return encodedString


    
    def decode(self, s: str) -> List[str]:
        
        decodedArr = []
        i = 0

        # 4#This2#Is1#A4#Test
        while i < len(s):
            j = i
            numStr = ""
            while s[j] != "#":
                numStr += s[j]
                j = j + 1
            
            decodedArr.append(s[j + 1 : j + int(numStr) + 1])
            i = j + 1 + int(numStr)
        
        return decodedArr

if __name__ == "__main__":


    solution = Solution()
    wordList = ["This", "Is", "A", "Test"]
    print("Original List: " + str(wordList))
    encodedStr = solution.encode(wordList)
    print("Encoded Word: " + encodedStr)
    decodedList = solution.decode(encodedStr)
    print("Decoded List: " + str(decodedList))