from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramDict = dict()
        groupArr = []

        for i in range(len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            if sortedStr not in anagramDict:
                anagramDict[sortedStr] = len(groupArr)
                groupArr.append([])
                
            groupArr[anagramDict[sortedStr]].append(strs[i])

        return groupArr
            



if __name__ == "__main__":

    solution = Solution()
    print(str(solution.groupAnagrams( strs = ["act","pots","tops","cat","stop","hat"] )))
    print(str(solution.groupAnagrams( strs = ["x"] )))
    

    