class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def traversal(self):
        if self.head is None:
            print("The linkedlist is empty: ")
        else:
            n=self.head
            while n:
                print(n.data,"-->",end=" ")
                n=n.next
                if n==self.tail.next:
                    break
            print()
    def btraversal(self):
        if self.tail is None:
            print("The linkedlist is empty: ")
        else:
            n=self.tail
            while n:
                print(n.data,"-->",end=" ")
                n=n.prev
                if n==self.head.prev:
                    break
            print()
    def insertion(self,item,location):
        newnode=Node(item)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                newnode.prev=self.tail
                self.head.prev=newnode
                self.head=newnode
                self.tail.next=newnode
            elif location == 1:
                newnode.prev=self.tail
                newnode.next=self.head
                self.head.prev=newnode
                self.tail.next=newnode
                self.tail=newnode
            else:
                index=0
                node=self.head
                while index<location-1:
                    node=node.next
                    index+=1
                newnode.next=node.next.next
                newnode.prev=node
                newnode.next.prev=newnode
                node.next=newnode
    def deletion(self,location):
        if self.head is None:
            print("The linked list is empty: ")
        elif self.head==self.tail:
            self.head.prev=None
            self.tail.next=None
            self.head=None
            self.tail=None
        else:
            if location == 0:
                self.head=self.head.next
                self.head.prev=self.tail
                self.tail.next=self.head
            elif location == 1:
                self.tail=self.tail.prev
                self.tail.next=self.head
                self.head.prev=self.tail
            else:
                index=0
                n=self.head
                while index < location-1:
                    n=n.next
                    index+=1
                nextnode=n.next.next
                nextnode.prev=n
                n.next=nextnode
    def searching(self,item):
        if self.head is None:
            print("The linked list is empty: ")
        else:
            n=self.head
            while n:
                if n.data==item:
                    print("Yes the value found: ")
                    break
                n=n.next
cdll=linkedlist()
num=list(map(int,input("enter the elements: ").split(" ")))
for i in num:
    cdll.insertion(i,1)
cdll.traversal()
ele=int(input("enter the elem location for del: "))
cdll.deletion(ele)
cdll.traversal()
el=int(input("enter the ele for searching: "))
cdll.searching(el) 
cdll.btraversal()
cdll.traversal()                   
