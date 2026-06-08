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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        newHead = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return newHead



if __name__ == "__main__":

    solution = Solution()

    print([1,2,3,4,5])
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head.print()
    head = solution.reverseList( head )
    head.print()

    

    