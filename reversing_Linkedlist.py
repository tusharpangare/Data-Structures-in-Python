# for ref: https://www.youtube.com/watch?v=ugQ2DVJJroc

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList():
    def __init__(self):
        self.head=None

    def insert_node(self, data):
        if self.head is None:
            self.head=Node(data, None)
            return

        itr=self.head
        while itr:
            temp=itr.next
            if temp is None:
                itr.next=Node(data, None)  
                break
            itr=itr.next
        
    # reversing using iterative method
    def reverse_LL(self):
        current=self.head
        prev=None
        while current !=None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev        

    def print_LL(self):
        if self.head is None:
            print("LL is empty")
            return
        itr=self.head
        while itr:
            print(str(itr.data),end="-->")
            itr=itr.next
        print()    


LL=LinkedList()
LL.insert_node(10)                         
LL.insert_node(20)                         
LL.insert_node(30)                         
LL.insert_node(40) 
LL.print_LL()        
LL.reverse_LL()
LL.print_LL()                