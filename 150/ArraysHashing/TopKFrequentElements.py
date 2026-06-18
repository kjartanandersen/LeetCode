from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = dict()
        topKNums = []

        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1

        numsDict = dict(sorted(numsDict.items(), key=lambda item: item[1], reverse=True))

        it = 0
        for key in numsDict:
            topKNums.append(key)
            it += 1
            if it == k:
                return topKNums
            
        return topKNums

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.topKFrequent( nums = [1,2,2,3,3,3], k = 2 )))
    print(str(solution.topKFrequent( nums = [7,7], k = 1 )))
    

    