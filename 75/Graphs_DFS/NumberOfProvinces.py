from collections import deque
from typing import List, Optional

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        provinces = 0

        def dfs(city: int):
            visited.add(city)
            for i in range(len(isConnected[city])):
                if isConnected[city][i] and i not in visited:
                    dfs(i)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces


if __name__ == "__main__":

    solution = Solution()

    print(solution.findCircleNum( isConnected = [[1,1,0],[1,1,0],[0,0,1]] ))
    print(solution.findCircleNum( isConnected = [[1,0,0],[0,1,0],[0,0,1]] ))
    print()
    print()

    
    
    

    
