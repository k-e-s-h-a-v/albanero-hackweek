# Q.47 Check if a given linked list is Palindrome or not. 
# If yes return "True" otherwise "False". Expamples:
# Input:  1->2->3->2->1
# Output: True
# Input: 1->2->3->1->2
# Output: False



class Node:
    def __init__(self, data = None, next=None, prev=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):    
        self.head = None
        self.tail = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = newNode

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def palindromeCheck(self, n):
        if not (self.head):
            return
        current = self.head
        currentB = self.tail
        for i in range(n//2):
            if current.data == currentB.data:
                current.next = current.next.next
                currentB = self.get_prev_node(currentB)
            else:
                return False
        return True

    def DisplayLinkedList(self):
        current = self.head
        while(current):
            print(current.data,end=' -> ')
            current = current.next
        print('None')

listwa = LinkedList()

print('Enter list (one element at a time)')
count = 0
while True:
    digit = input("-> ")
    if not digit: break
    listwa.insert(int(digit))
    count += 1
    
print('The list is',end=' ')
listwa.DisplayLinkedList()
print('Palindrome ? ',listwa.palindromeCheck(count))
