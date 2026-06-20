
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        leftPtr = 0
        rightPtr = len(s)-1

        while leftPtr < rightPtr:
            while leftPtr < rightPtr and not s[leftPtr].isalnum():
                leftPtr += 1
            while leftPtr < rightPtr and not s[rightPtr].isalnum():
                rightPtr -= 1

            if leftPtr < rightPtr:
                if s[leftPtr].lower() != s[rightPtr].lower():
                    return False
            leftPtr += 1
            rightPtr -= 1

        return True

if __name__ == "__main__":

    solution = Solution()
    print(str(solution.isPalindrome( s = "Was it a car or a cat I saw?" )))
    print(str(solution.isPalindrome( s = "tab a cat" )))
    print(str(solution.isPalindrome( s = "??Was it a car or a cat I saw???" )))
    print(str(solution.isPalindrome( s=".," )))
    

    