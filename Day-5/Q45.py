# Q.45 Remove the duplicate nodes from the sorted Linked list. 
# The list should only be traversed once. 
# Examples:
# Input: 1->1->2->2->3->4->5->5
# Output: 1->2->3->4->5
# Input: 12->15->15->17->17->19
# Output: 12->15->17->19
# Note: Linked list is already sorted. You can traverse Linked list only once.


class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):    
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def mySet(self):
        if not (self.head):
            return
        current = self.head
        while(current.next):
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def DisplayLinkedList(self):
        current = self.head
        while(current):
            print(current.data,end=' -> ')
            current = current.next
        print('None')

listwa = LinkedList()

print('Enter list (one element at a time)')
while True:
    digit = input("-> ")
    if not digit: break
    listwa.insert(int(digit))
    
print('The list before duplicate removal ',)
listwa.DisplayLinkedList()
print()

print('The list after removing duplicates ')
listwa.mySet()
listwa.DisplayLinkedList()