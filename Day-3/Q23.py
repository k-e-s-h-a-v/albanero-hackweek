# Q23. Create a singly linked-list. The list can be represented as:
#   L0 -> L1 -> … → Ln - 1 -> Ln
#   Reorder the list to be in the following form:
#   L0 -> Ln -> L1 → Ln - 1 -> L2 -> Ln - 2 -> …
#   You can not modify the values in the list's nodes. 
#   Only nodes themselves can be changed.
#   Expamples:
#   Input: 1->2->3->4
#   Output: 1->4->2->3
#   Input: 1->2->3->4->5
#   Output: 1->5->2->4->3

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
    
print('The list before rearrangement ',)
listwa.DisplayLinkedList()
print()

print('The list after rearrangement ')
listwa.oddEven()
listwa.DisplayLinkedList()    