# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        values = []
        while head.next is not None:
            values.append(head.val)
            head = head.next
        temp = head
        for i in range(len(values)-1, -1, -1):
            new_node = ListNode(values[i])
            temp.next = new_node
            temp = new_node

        return head

    def reverseListOptimized(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
            