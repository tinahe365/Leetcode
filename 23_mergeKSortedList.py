import heapq
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                # heapq.heappush(heap, node.val)
                heapq.heappush(heap, (node.val,i,node))
                print(heap)
        
        dummy = ListNode()
        cur = dummy

        while heap:
            val,i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
            print(cur)

        return dummy.next

def main():
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    
    solution = Solution()
    merged_list = solution.mergeKLists(lists)
    
    # Print the merged list
    cur = merged_list
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

if __name__ == "__main__":
    main()