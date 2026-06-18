from collections import deque
from typing import List, Optional




class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visitedRooms = set()

        stack = [0]
        visitedRooms.add(0)

        while stack:
            room = stack.pop()

            for i in range(len(rooms[room])):
                if rooms[room][i] not in visitedRooms:
                    visitedRooms.add(rooms[room][i])
                    stack.append(rooms[room][i])

        return len(visitedRooms) == len(rooms)

if __name__ == "__main__":

    solution = Solution()

    print(solution.canVisitAllRooms( rooms = [[1],[2],[3],[]] ))
    print(solution.canVisitAllRooms( rooms = [[1,3],[3,0,1],[2],[0]] ))
    print()
    print()

    
    
    

    
