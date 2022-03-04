class Node:
    # creating a node with two fields data and next
    # initially both assigned as null(None)
    def __init__(self, data= None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self, data):
        # if LL is empty
        if self.head is None:
            self.head=Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)    

    def get_len(self):
        if self.head is None:
            return 0
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count    

    def print_middle(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        print("middle element is ", str(slow_ptr.data))    

    '''def print_middle(self):
        # this method is by tushar (complexity issues 🙂)
        len=self.get_len()
        if len==0:
            print("LL is empty")
            return
        if len==1:
            print(f"middle element is {self.head.data}" )
            return
        index=(len//2)+1   
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                print(f"middle element is {itr.data}")
            itr=itr.next
            count+=1
            '''

    def print_LL(self):
        if self.head is None:
            print("LL is empty")
            return
        ll_str=""
        itr=self.head
        while itr:
            ll_str+=str(itr.data)+"-->" 
            itr=itr.next
        print(ll_str)


ll=LinkedList()
ll.insert_at_end(10)                      
ll.insert_at_end(20)                      
ll.insert_at_end(30)                      
ll.insert_at_end(40)    
# ll.insert_at_end(50)    
ll.print_LL() 
ll.print_middle()              