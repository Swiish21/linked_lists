# this class is specifically used to when the linked list class below needs to create a new node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    #below is a constructor for a new node in a linked list with no other nodes in it(empty LL).
    def __init__(self, value):
        new_node = Node(value) #node class is called and constructs a new node with a value(a variable named value with a value)
        self.head = new_node #shows which node the head of the linked list will point
        self.tail = new_node #shows also which node the tail of the ll will point
        self.length = 1  #shows the length of LL for keep track purposes.

#below we have defined a variable and using the above 2 methods to create a 1 node long linked list with a value of 4
#we called the LinkedList class and used its method create a LL one node long        
my_linkedList = LinkedList(4)
# my_linkedList = LinkedList()

#to print the value of a certain node in a LL we do it the way shown below
#var name of the LL, then head and its value(for a longer LL we use sth different)
print(my_linkedList.head.value)
print(my_linkedList.tail.value)
print(my_linkedList.length)