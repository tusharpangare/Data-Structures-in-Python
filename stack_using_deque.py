# we'll implement stack using deque
from collections import deque
# user defined exception for an empty stack
class EmptyStackError(Exception):
    """Stack is empty"""
    pass


class Stack:
    # here container is just a name given to the stack, you can change if you want to
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError
        # return the popped element  
        return self.container.pop()

    # peek will return the top value of the stack
    def peek(self):
        return self.container[-1]

    # is_empty will return true if stack is empty
    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container) 

    def display(self):
        print(self.container)
    

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(stack.peek())
try:
    print("popping elements from stack")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
except EmptyStackError as e:
    print(e.__doc__)

print(stack.size())
stack.display()    




