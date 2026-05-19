from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat or not mat[0]:
            return []

        maxRow, maxCol = len(mat), len(mat[0])
        result = [0] * (maxRow * maxCol)
        resIdx = 0
        row = col = 0

        for _ in range(maxRow * maxCol):
            result[resIdx] = mat[row][col]
            resIdx += 1

            if (row + col) % 2 == 0:
                if col == maxCol - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1

            else:
                if row == maxRow - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1
        
        return result
            


if __name__ == "__main__":
    solution = Solution()
    print(str(solution.findDiagonalOrder(  [[1,2,3],[4,5,6],[7,8,9]]  )))