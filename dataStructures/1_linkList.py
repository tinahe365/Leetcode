class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        pass
    def insert(self, value):
        pass

my_linked_list = LinkedList(4)

my_linked_list.append(5)
my_linked_list.print_list()


    # def __init__(self):
    #     self.head = None

    # def append(self, value):
    #     new_node = Node(value)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     last_node = self.head
    #     while last_node.next:
    #         last_node = last_node.next
    #     last_node.next = new_node

    # def display(self):
    #     current_node = self.head
    #     values = []
    #     while current_node:
    #         values.append(current_node.value)
    #         current_node = current_node.next
    #     print(" -> ".join(map(str, values)))
   