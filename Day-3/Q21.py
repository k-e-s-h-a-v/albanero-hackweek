'''
Q21. Create a singly linked list. 
Group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as 
it was in the input.
Expamples:
Input:  1->2->3->4->5
Output: 1->3->5->2->4
Input: 2->1->3->5->6->4->7
Output: 2->3->6->7->1->5->4
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


    def oddEven(self):
        if not (self.head):
            return

        oddCurrent = self.head
        evenCurrent = self.head.next
        evenFirst = evenCurrent
        
        while True:
            if (oddCurrent == None or evenCurrent == None or evenCurrent.next == None):               
                oddCurrent.next = evenFirst
                break
            oddCurrent.next = evenCurrent.next
            oddCurrent = evenCurrent.next
            if (oddCurrent.next == None):
                evenCurrent.next = None
                oddCurrent.next = evenFirst
                break
            evenCurrent.next = oddCurrent.next
            evenCurrent = oddCurrent.next 
    
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
