# singly linked list


# from node import Node


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
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
    def traverse(self):
        if self.head is None:
            print('list is empty')
            
        else:
            curr=self.head
            while curr is not None:
                print(curr.value)
                curr=curr.next


list1=SinglyLinkedList()
list1.append(5)
list1.append(6)
list1.append(7)
list1.traverse()





