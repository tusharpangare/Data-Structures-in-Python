#binary tree using LinkedList 
class Node:
    def __init__(self, data) :
        self.data=data
        self.left=None
        self.right=None

# inorder traversal of binary tree
def print_inorder(root):
    if  root:
        # first recur on left child
        print_inorder(root.left)
        
        # print data of node
        print(root.data, end=" ")

        # recur on the right child
        print_inorder(root.right)  

def print_preorder(root):
    if root:
        # first print data of node
        print(root.data, end=" ")

        # recur on left child
        print_preorder(root.left)

        # recur on right child
        print_preorder(root.right)


def print_postorder(root):
    if root:
        # first recur on left child
        print_postorder(root.left)

        # recur on right child
        print_postorder(root.right)

        # print data of node
        print(root.data, end=" ")    

'''
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is NULL
    4) If current is NULL and stack is not empty then 
        a) Pop the top item from stack.
        b) Print the popped item, set current = popped_item->right 
        c) Go to step 3.
    5) If current is NULL and stack is empty then we are done.
    '''
# iterative inorder traversal with stack
def in_order(root):
    
    # initialize current with root
    current=root
    # initialize stack
    stack=[]
    
    while True:
        # reach the leftmost node of the current node
        if current is not None:
            # add current node into the stack
            stack.append(current)
            # goto left of cuurent
            current=current.left

        # if current is empty and stack is not empty then 
        elif stack:
            # pop out the stack element and make current to the popped out element
            current=stack.pop()
            #print the popped item
            print(current.data, end=" ") 
            # set current to  right of popped item
            current=current.right

        # if current and stack both are empty then we are done
        else:
            break        
        

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

'''
# tree will be like:   
                        1

                    2       3
                    
                4       5        

'''

print("Inorder Traversal using recursive method:")
print_inorder(root)
print()

print("Preorder Traversal using recursive method:")
print_preorder(root)
print()

print("Postorder Traversal using recursive method:")
print_postorder(root)
print()

print("Inorder Traversal using iterative method: ")
in_order(root)
print()