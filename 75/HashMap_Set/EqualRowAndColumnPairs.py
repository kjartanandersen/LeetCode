from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        tPose = Counter(zip(*grid))
        grid = Counter(map(tuple, grid))

        return sum(tPose[t]*grid[t] for t in tPose)
    

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.equalPairs( grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] )))
    

    