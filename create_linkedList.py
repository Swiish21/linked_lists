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

    def print_linkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append (self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

my_linkedList = LinkedList(4)

my_linkedList.append(3)
my_linkedList.append(2)


my_linkedList.print_linkedList()

#fully functional linked list
        
