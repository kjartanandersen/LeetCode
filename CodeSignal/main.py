
from typing import List

class Q1:
    def arrayManipulation(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        sumArr = [0] * n
        for i in range(n):

            if (i == 0):
                sumArr[i] = arr[i] + arr[i+1]
            elif (i == n-1):
                sumArr[i] = arr[i-1] + arr[i]
            else:
                sumArr[i] = arr[i-1] + arr[i] + arr[i+1]
            
        return sumArr

        


if __name__ == "__main__":

    q1 = Q1()
    arr = [4, 0, 1, -2, 3 ]
    print(f"Array Before: {arr}")
    print(f"Array After: {q1.arrayManipulation(arr)}")
    pass