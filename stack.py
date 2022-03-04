class Error(Exception):
    '''Base class for user defined exception'''
    pass

class EmptyError(Error):
    '''Stack is empty'''
    pass

# stack using List
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print("Initial stack:",stack,sep="\n")
print("Elements popped from stack:")
try:
    while stack!=[]:
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
    raise EmptyError    
except EmptyError as e:
    print("empty")
