import sys
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left, right = dummy, dummy

        for i in range(n+1):
            right = right.next
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)
    
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    main()