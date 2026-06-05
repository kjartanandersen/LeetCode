from typing import List
from collections import deque

class RecentCounter:

    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1
        return len(self.records) - self.start

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



if __name__ == "__main__":

    solution = RecentCounter()
    print(str(solution.ping( t = 1 )))
    print(str(solution.ping( t = 100 )))
    print(str(solution.ping( t = 3001 )))
    print(str(solution.ping( t = 3004 )))
    print(str(solution.ping( t = 3006 )))
    print(str(solution.ping( t = 4001 )))
    print(str(solution.ping( t = 4002 )))
    print(str(solution.ping( t = 4003 )))
    print(str(solution.ping( t = 4004 )))
    print(str(solution.ping( t = 4006 )))
    print(str(solution.ping( t = 4010 )))
    print(str(solution.ping( t = 5002 )))
    print(str(solution.ping( t = 5003 )))
    print(str(solution.ping( t = 5005 )))
    print(str(solution.ping( t = 5006 )))
    

    