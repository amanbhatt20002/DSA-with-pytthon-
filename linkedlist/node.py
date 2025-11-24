# introduction to linked list 
#  making  first node

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

node1=Node(5)
node2=Node(6)
node3=Node(7)
node4=Node(8)
node5=Node(3)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
print(node1.next)
print(node2.next)
print(node3.value)
print(node4.value)
print(node5.value)

print("..............................................................................")
print(node1.next.next.next.next.value)