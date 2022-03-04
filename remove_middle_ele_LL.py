class Node:
    def __init__(self, data=None, next= None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)
    def remove_middle_ele(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while fast_ptr and  fast_ptr.next:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        data=slow_ptr.data    
        itr=self.head
        while itr:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next       

    def print_LL(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr=self.head
        ll_str=""
        while itr:
            ll_str+=str(itr.data)+"-->"
            itr=itr.next
        print(ll_str)      

ll=LinkedList()
ll.insert_at_end(10)                   
ll.insert_at_end(20)                   
ll.insert_at_end(30) 
ll.insert_at_end(40) 
ll.print_LL()
ll.remove_middle_ele()
ll.print_LL()                  