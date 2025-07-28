# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy

        def getKth(node):
            for i in range(k):
                if not node:
                    return None
                node = node.next
            return node

        def reverseBlock(prev: ListNode, kth: ListNode) -> ListNode:
            groupNext = kth.next

            # reverse
            curr = prev.next
            while curr.next is not groupNext:
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            # return the new link list of the next group, head is the last node of the previous group
            return curr

        while True:
            k_thNode = getKth(prev)
            if not k_thNode:
                break
            prev = reverseBlock(prev, k_thNode)

        return dummy.next

        

        
        




        
        


        


        