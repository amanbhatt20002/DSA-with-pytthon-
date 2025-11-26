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
                print(curr.value,end=",")
                curr=curr.next
    def insert(self,value,pos):
        new_node=Node(value)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            prev=None
            count=0
            while curr is not None and count<pos-1:
                prev=curr
                curr=curr.next
                count+=1
            prev.next=new_node
            new_node.next=curr
    def delete(self,key):
        curr=self.head
        if curr and curr.value==key:
            self.head=curr.next
            return
        prev=None
        while curr and curr.value!=key:
            prev=curr
            curr=curr.next
        if curr:
            prev.next=curr.next





        
        
       





list1=SinglyLinkedList()
list1.append(5)
list1.append(6)
list1.append(7)
list1.append(5)
list1.append(7)
list1.insert(55,3)
list1.insert(56,3)
list1.delete(56)
list1.insert(56,3)

list1.traverse()





