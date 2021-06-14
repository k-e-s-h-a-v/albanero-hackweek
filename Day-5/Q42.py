# Q.42 Reverse the given Linked list.
# Examples:
# Input : 1->2->3->4->5
# Output: 5->4->3->2->1
# Input : 1->3->5->7
# Output: 7->5->3->1
# note: you need to reverse the node itself, not the data part.


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

    def reverse(self):
            prev = None
            current = self.head
            while(current):
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev
    
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
    
print('The list before reversing ',)
listwa.DisplayLinkedList()
print()

print('The list after reversing ')
listwa.reverse()
listwa.DisplayLinkedList()