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
            print(str(it.val) + " ", end="")
            it = it.next

        print("")

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head

        oddIt = head
        evenIt = head.next
        evenHead = head.next

        while (evenIt != None and evenIt.next != None):
            oddIt.next = evenIt.next
            oddIt = oddIt.next
            evenIt.next = oddIt.next
            evenIt = evenIt.next

        oddIt.next = evenHead

        return head


if __name__ == "__main__":

    solution = Solution()

    print([1,2,3,4,5])
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head.print()
    solution.oddEvenList( head )
    print()
    head.print()

    

    