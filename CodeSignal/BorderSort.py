

from typing import List, Hashable

class Solution:
    def kBorderSort(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    matrix[i][j] *= -1

        matrix.sort(key=lambda x: (x[0], x[-1]))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    matrix[i][j] *= -1

        return matrix
    
    def amountIlluminatedOnce(self, lamps: List[List[int]])-> int:
        
        illumPos = {}
        isOneCount = 0
    
        for i in range(len(lamps)):
            
            for j in range(lamps[i][0] - lamps[i][1], lamps[i][0] + lamps[i][1] + 1):
                if j not in illumPos:
                    illumPos[j] = 0
                illumPos[j] += 1
                if illumPos[j] == 1:
                    isOneCount += 1
                else:
                    isOneCount -= 1
        
        return isOneCount
    
if __name__ == "__main__":
    matrix = [[-2, 3], [2, 3], [2, 1]]
    
    solution = Solution()
    result = solution.amountIlluminatedOnce(matrix)

    print(f"Output should be: {6}")
    print(result)

