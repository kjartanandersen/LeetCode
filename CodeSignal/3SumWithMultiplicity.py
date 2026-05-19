

from typing import List, Hashable

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        n = len(arr)

        ans = 0

        mod = int(1e9 + 7)

        mpp = {}

        for i in range(n):
            for j in range(i+1, n):
                need = target - arr[i] - arr[j]
                if need in mpp:
                    ans += mpp[need]
                else:
                    mpp[need] = 0
            mpp[arr[i]] = mpp.get(arr[i], 0) + 1

        return ans % mod
        



if __name__ == "__main__":

    solution = Solution()
    print(solution.threeSumMulti(  [1,1,2,2,3,3,4,4,5,5], 8  ))