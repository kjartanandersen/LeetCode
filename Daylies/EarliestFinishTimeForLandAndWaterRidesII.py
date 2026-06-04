from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        l = w = landMin = waterMin = 10e5


        for i in range(len(landStartTime)):
            l = min(l, landStartTime[i] + landDuration[i])

        for i in range(len(waterStartTime)):
            w = min(w, waterStartTime[i] + waterDuration[i])
            landMin = min(landMin, max(waterStartTime[i], l) + waterDuration[i])
        
        for i in range(len(landStartTime)):
            waterMin = min(waterMin, max(landStartTime[i], w) + landDuration[i])

        return min(landMin, waterMin)

        
    
if __name__ == "__main__":

    solution = Solution()
    print(str(solution.earliestFinishTime( landStartTime = [100000], landDuration = [100000], waterStartTime = [100000], waterDuration = [100000] )))
    

    