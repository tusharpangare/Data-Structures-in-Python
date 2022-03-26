#binary tree using LinkedList 
class Node:
    def __init__(self, key) :
        self.val=key
        self.left=None
        self.right=None

# inorder traversal of binary tree
def print_inorder(root):
    if  root:
        # first recur on left child
        print_inorder(root.left)
        
        # print data of node
        print(root.val)

        # recur on the right child
        print_inorder(root.right)  

def print_preorder(root):
    if root:
        # first print data of node
        print(root.val)

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
        print(root.val)    
        

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

print("Inorder TRaversal:")
print_inorder(root)

print("Preorder Traversal")
print_preorder(root)

print("Postorder Traversal")
print_postorder(root)

