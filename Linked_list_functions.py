class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def check_empty(self):
        if self.head is None:
            return True
        return False

    def insert(self, data):
        if self.head is None:
            self.head=Node(data, None) 
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)

    def search_by_data(self, data):
        '''here, if data is found then we'll return it's index position'''
        if not self.head:
            print("LL is empty, can't perform search")
            return
        position=0
        itr=self.head
        while itr:
            if itr.data==data:
                print(f"data present at index:{position}")   
                break
            position+=1
            itr=itr.next 
        else:
            print("data not present") 


    def find_ref_to_node(self, data):
        '''here we'll find the next reference of given data'''
        if self.head is None:
            print("LL is empty")
            return
        itr=self.head
        while itr:
            if itr.data==data:
                if itr.next is None:
                    print("Current node is pointing to None") 
                    break
                print("Current node is pointing to:", str(itr.next.data)) 
                return
            itr=itr.next


    def insert_after_given_node(self,node_data,insert_data ):
        try:
            assert self.head is not None
        except AssertionError:
            print("LL is empty")   
        else:     
            itr=self.head
            while itr:
                if itr.data == node_data:
                    node=Node(insert_data, itr.next)
                    itr.next=node
                    break
                itr=itr.next    
    def delete_at_beginning(self):
        if self.head is None:
            print("LL is empty")
            return
        self.head=self.head.next   

    def deletion_last_node(self):
        if self.head is None:
            print("LL is empty")
            return

        itr=self.head
        while itr:
            if itr.next.next is None:
                itr.next=None
            itr=itr.next
             
    def delete_node(self, data):
        if self.head is None:
            print("LL is empty")
            return
        itr=self.head
        
        if self.head.data==data:
            self.head=self.head.next
            return

        while itr:
            if itr.next is None:
                print("value not available in the LinkedList")
                break
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next
        else:
            print("data not founds")  
                 
    def find_miidle(self):
        if self.head is None:
            print("LL is empty")
            return
        slow_ptr=self.head
        fast_ptr=self.head

        while fast_ptr and fast_ptr.next:
            # if fast_ptr.next.next is None:
            #     print("middle of LL is", str(slow_ptr.data))
            #     break
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next    
        print("middle of LL is", str(slow_ptr.data))   

    def get_len(self):
        if self.head is None:
            return 0
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count    

    def reverse_LL(self):
        current=self.head
        prev=None
        while current !=None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev  


    def display_LL(self):
        if self.head is None:
            print("LL is empty")
            return
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            # print("%d"%(itr.data),end="-->")
            itr=itr.next
        print()    
'''
LL=LinkedList()
LL.insert(10)                                              
LL.insert(20)                                              
LL.insert(30)                                              
LL.insert(40) 
LL.insert(50) 
LL.insert(60) 
LL.display_LL()   
LL.search_by_data(30)   
LL.find_ref_to_node(20)    
# print(LL.find_ref_to_node.__doc__)                                   
LL.insert_after_given_node(10, 15)
LL.display_LL()
LL.delete_at_beginning()
LL.display_LL()
LL.deletion_last_node()
LL.display_LL()
LL.delete_node(20)
LL.display_LL()
LL.find_miidle()
print(LL.get_len())'''

LL=LinkedList()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
LL.reverse_LL()
LL.display_LL()

# LL.insert(10)                                              
# LL.insert(20)                                              
# LL.insert(30)                                              
# LL.insert(40) 
# LL.find_miidle()