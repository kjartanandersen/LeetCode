from collections import deque
from typing import Deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        qr: Deque[int] = deque()
        qd: Deque[int] = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                qr.append(i)
            else:
                qd.append(i)
        
        n = len(senate)

        while qr and qd:
            rPos = qr.popleft()
            dPos = qd.popleft()

            if rPos < dPos:
                qr.append(rPos + n)
            else:
                qd.append(dPos + n)

        return "Radiant" if qr else "Dire"


if __name__ == "__main__":

    solution = Solution()
    print(str(solution.predictPartyVictory( senate = "RDD" )))

    

    