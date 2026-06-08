from collections import deque
from typing import Deque, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        it = head

        while (it != None):
            print(str(it.val) + " ")
            it = it.next



class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return None

        retHead = head

        singleIt = head
        doubleIt = head

        while (doubleIt.next != None):
            if(doubleIt.next.next == None):
                break
            doubleIt = doubleIt.next.next
            if doubleIt.next != None:
                singleIt = singleIt.next

        singleIt.next = singleIt.next.next

        return retHead
        


if __name__ == "__main__":

    solution = Solution()

    print([1,3,4,7,1,2,6])
    head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    head.print()
    solution.deleteMiddle( head )
    print()
    head.print()
    
    print()
    print([1,2,3,4])
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    head.print()
    solution.deleteMiddle( head )
    print()
    head.print()

    print()
    print([2, 1])
    head = ListNode(2, ListNode(1))
    head.print()
    solution.deleteMiddle( head )
    print()
    head.print()

    print()
    print([1])
    head = ListNode(1)
    head.print()
    solution.deleteMiddle( head )
    print()
    head.print()
    

    