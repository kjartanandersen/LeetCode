from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        it = head

        while (it != None):
            print(str(it.val) + " ", end="")
            it = it.next

        print("")



class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Two pointer
        
        single = head
        double = head

        prev = None

        while double and double.next:
            double = double.next.next


            temp = single.next
            single.next = prev  
            prev = single
            single = temp

        retVal = 0

        while single:
            retVal = max(prev.val + single.val, retVal)
            prev = prev.next
            single = single.next

        return retVal

        # Stack
        
        # listStack = []
        # def getListLength(head: Optional[ListNode]) -> int:
        #     it = head
        #     num = 0
        #     while (it != None):
        #         num += 1
        #         it = it.next
        #     return num
        
        # nHalf = getListLength(head) / 2
        # it = head
        # num = 0
        # maxVal = 0
        # while it != None:
        #     if num < nHalf:
        #         listStack.append(it.val)

        #     else:
        #         maxVal = max(listStack.pop() + it.val, maxVal)

        #     num += 1
        #     it = it.next
        
        # return maxVal
    
if __name__ == "__main__":

    solution = Solution()

    head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    head.print()
    print(solution.pairSum( head ))

    print()

    head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    head.print()
    print(solution.pairSum( head ))

    print()

    head = ListNode(1, ListNode(100000))
    head.print()
    print(solution.pairSum( head ))

    print()

    head = ListNode(5, ListNode(4, ListNode(10, ListNode(20, ListNode(30, ListNode(2))))))
    head.print()
    print(solution.pairSum( head ))
    
    
    

    