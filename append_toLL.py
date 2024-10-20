#this class is used to create a new node when called upon..
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#this method is used to add items to the last node of a linked list..
#if there's no nodes in the linked list, it will take the new node created and point the head and tail pointers and point it to the new node, creating a 1 length linked list.
def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
#in this else statement, if there's already a linked list in place with nodes, it takes the value of the last node pointer(none) and points it to the new node, then moves the tail pointer to the new node created.
#the last line of code(20) just updates the lenth of the LL to add one more.
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
