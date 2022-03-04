# single linked list
# take reference:https://www.youtube.com/watch?v=qp8u-frRAnU
# forst we'll create a class to create nodes

class Node:
    def __init__(self,data=None, next=None):
        self.data=data      #assigning data to the data variable
        self.next=next      #initializing next node as null (None in python)

# creating class for linked list
class LinkedList:
    def __init__(self):
        self.head=None   #initializing head pointer
    
    def insert_at_beginning(self, data):
        node=Node(data,self.head)      #next will point to head of next node
        self.head=node                #head will point to new node which is inserted at beginning

    def insert_at_end(self,data):
        # if L_list is empty insert at beginning
        if self.head is None:
            self.head=Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        #at the end of the while loop, itr.next will be pointing to None
        # that means we reached the end of the linkedlist
        # now we'll create a new node from our given data and will assign to the itr.next
        # that means itr.next will point to our node
        itr.next=Node(data, None)      

    def insert_values(self, data_list):
        # here we'll be converting list in LinkedList
        self.head=None #wiping out existing data
        for data in data_list:
            self.insert_at_end(data)  

    def get_len(self):
        # we'l count the total no of heads present in the LL
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next  
        return count      

    def remove_at_index(self,index):
        if index<0 or index>=self.get_len():
            # raise Exception("Invalid Index")
            print('Invalid Index')
            return 
        if index==0:
            self.head=self.head.next
            return

        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1            
    def insert_at_index(self, index, data):
        if index<0 or index>=self.get_len():
            # raise Exception("Invalid Index")
            print('Invalid Index')
            return 
        if index==0:
            self.insert_at_beginning(data)
            return 
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                temp=itr.next
                itr.next=Node(data, temp)
                del temp
                break
            itr=itr.next
            count+=1            


    def print_LL(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            itr=self.head
            ll_str=""
            while itr:
                ll_str+=str(itr.data)+"-->"
                itr=itr.next
            print(ll_str)

if __name__=="__main__":
    '''ll=LinkedList()
    ll.insert_values(["abc","pqr","xyz","hex","dec"])
    # ll.remove_at_index(-1)
    ll.insert_at_index(2, "banana")
    ll.print_LL()'''

    ll=LinkedList()
    ll.insert_values([7,5,2,63,15,98,12])
    ll.remove_at_index(1)
    ll.insert_at_index(2, 55)
    ll.print_LL()

    '''ll=LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.remove_at_index(2)
    ll.insert_at_index(3, 156)
    ll.print_LL()'''


'''
class Node:
    def __init__(self, data=None, next= None):
        self.data=data
        self.next=next
class LinkedList():
    def __init__(self):
        self.head=None

    def insert_at_end(self, data):
        node=Node(data, None)
        itr=self.head
        # if list is empty node will get added at beginning
        if itr is None:
            self.head=node
        else:
            # if list is not empty we'll traverse till the end of the list
            while itr:
                if itr.next is None:       #at the end of the Linkedlist, next points to None
                    #now we'll assign our node to next , bcz we're insering at end
                    itr.next=node 
                    break
                itr=itr.next          

    def print_LL(self):
        itr= self.head
        if itr is None:
            print("LinkedList is empty")
            return 
        else:    
            ll_str=""
            while itr:
                ll_str+=str(itr.data)+"-->"
                itr=itr.next
            print(ll_str)

ll=LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.print_LL()


'''