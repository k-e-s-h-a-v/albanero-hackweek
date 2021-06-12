'''
Q22. Create a singly linked list. 
Swap every two adjacent nodes and return the reordered list.
  Expamples:
  Input: 1->2->3->4
  Output: 2->1->4->3
  Input:  1
  Output: 1
'''


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

    def swapper(self):
        current = self.head
        if not current:
            return 
        while(current and current.next):
            if(current.data != current.next.data):
                current.data, current.next.data = current.next.data, current.data
            current = current.next.next    
    
    def DisplayLinkedList(self):
        current = self.head
        while(current):
            print(current.data,end=' -> ')
            current = current.next
        print('None')

listForSwap = LinkedList()

print('Enter list for swapping one element at a time')
while True:
    digit = input("-> ")
    if not digit: break
    listForSwap.insert(int(digit))
    
print('The list before swap is ',)
listForSwap.DisplayLinkedList()
print()

print('The list after swap is ')
listForSwap.swapper()
listForSwap.DisplayLinkedList()