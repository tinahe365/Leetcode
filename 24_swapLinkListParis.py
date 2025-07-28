from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        cur = self
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("Null")

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify edge cases (e.g. swapping at the head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # As long as there are at least two more nodes to swap:
        while prev.next and prev.next.next:
            first  = prev.next
            print("fisrt:")
            first.print()
           
            second = first.next
            print("second:")
            second.print()
          
            # --- perform the swap ---
            prev.next     = second      # link previous to second
            first.next    = second.next # first now skips over second
            second.next   = first       # second now points to first
            
            
            # --- move prev to the end of this swapped pair ---
            prev = first
            print("prev:")
            prev.print()
            print("dummy:")
            dummy.print()
        
        return dummy.next
    

def main():
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # head.print()
    solution = Solution()
    swapped_head = solution.swapPairs(head)
   


if __name__ == "__main__":
    main()