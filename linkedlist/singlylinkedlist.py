# singly linked list


from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,value):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode

list1=SinglyLinkedList()
list.append(5)
list.append(6)




