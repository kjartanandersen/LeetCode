from collections import deque
from typing import List, Optional

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = { (a,b) for a,b in connections }
        neighbours = { city:[] for city in range(n) }
        visit = set()
        changes = 0

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):
            nonlocal edges, neighbours, visit, changes

            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue

                if (neighbour, city) not in edges:
                    changes += 1
                visit.add(neighbour)
                dfs(neighbour)

        visit.add(0)
        dfs(0)

        return changes



if __name__ == "__main__":

    solution = Solution()

    print(solution.minReorder( n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]] ))
    print(solution.minReorder( n = 5, connections = [[1,0],[1,2],[3,2],[3,4]] ))
    print(solution.minReorder( n = 3, connections = [[1,0],[2,0]] ))
    print()
    print()

    
    
    

    
