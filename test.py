class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_node_by_value(head: ListNode, value: int) -> ListNode:
    while head and head.value == value:
        head = head.next
        print(f"Removed head node with value {value}")

# usage example
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
value_to_remove = 3
print("Original linked list:", head)
