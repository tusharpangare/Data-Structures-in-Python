# for garbege collection
import gc

class Node:
    def __init__(self, data= None, prev= None, next= None,):
        self.data=data
        self.next=next
        self.prev=prev

class Doubly_linked_list:
    def __init__(self):
        self.head=None


    def insert_at_beginning(self, data):
        # check if DLL is empty
        if self.head is None:
            # if empty insert at beginning
            node=Node(data, None, None)
            # now head will point to newly created node
            self.head=node
            return
        # if not empty create a node pointing to current head  
        node=Node(data,None, self.head )
        # now hwad will be marked as newly created node bcz we're inserting at beginning
        self.head=node

    def delete_beginning(self):
        if self.head is None:
            print("DLL is Empty")
            return
        self.head=self.head.next
        self.head.prev=None    

    def delete_end(self):
        if self.head is None:
            print("DLL is empty")
            return
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None             
    
    def insert_at_end(self, data):
        # check if DLL is empty
        if self.head is None:
            # if empty insert at beginning
            self.insert_at_beginning(data)
            return
        # if not empty, travese till end
        # head will be assigned to iterator
        itr=self.head
        # it will iterate untill itr.next points to None i.e. it has reached end
        while itr.next:
            # each step, next node will be assigned to iterator
            itr=itr.next

        # we've reached att end, so we'll create a new node 
        # whose prev will point to current last node(itr) and end will point to None
        node=Node(data, itr, None)
        itr.next=node

    def get_len(self):
        if self.head is None:
            return 0
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next    
        return count

    def delete_node_by_val(self, data):
        if self.head is None:
            print("DLL is empty")
            return
        # if data present at beginning    
        if self.head.data==data:
            self.delete_beginning()
            return

        itr=self.head 
        # if node is in between start and end
        while itr.next.next:
            if itr.next.data==data:
                temp=itr.next.next
                itr.next=itr.next.next
                temp.prev=itr
                return
            itr=itr.next

        # if node present at the end
        if itr.next.data==data:
            self.delete_end()
        else:
            print(f"node containing data {data} is not present in DLL")    
        gc.collect()

    def insert_after_node(self, node_data, insert_data):
        if self.head is None:
            print("DLL is empty")
            return
        itr=self.head
        while itr.next:
            if itr.data==node_data:
                temp=itr.next
                node=Node(insert_data, itr,itr.next)  
                itr.next=node
                temp.prev=node
                break
            itr=itr.next
        if itr.data==node_data:
            self.insert_at_end(insert_data)    
        else:
            print(f"node data {node_data} not present in DLL")    
                    

    def print_doubly_LL(self):
        # check if empty
        if self.head is None:
            print("Doubly LL is empty")
            return
        # if not empty, iterate and print
        itr=self.head
        while itr:
            print(str(itr.data),end="-->")
            itr=itr.next
        print()    

    def print_reverse_DLL(self):
        if self.head is None:
            print("DLL is empty") 
            return
        itr=self.head
        # here we'll get the last node
        while itr.next:
            itr=itr.next       
        # we have it as our last node 
        while itr:
            print(str(itr.data),end="-->")
            itr=itr.prev

'''DLL=Doubly_linked_list() 
DLL.insert_at_beginning(10)   
DLL.insert_at_beginning(20)       
DLL.insert_at_beginning(30)   
DLL.insert_at_beginning(40)           
DLL.print_doubly_LL()'''

DLL=Doubly_linked_list() 
DLL.insert_at_end(10)
DLL.insert_at_end(20)
DLL.insert_at_end(30)
DLL.insert_at_end(40)
DLL.insert_at_end(50)
DLL.print_doubly_LL()
DLL.insert_after_node(50, 60)
DLL.print_doubly_LL()
# DLL.delete_node_by_val(10)
# DLL.print_doubly_LL()
# DLL.print_doubly_LL()
# DLL.delete_beginning()
# DLL.delete_end()
# DLL.print_doubly_LL()
# print(DLL.get_len())
DLL.print_reverse_DLL()