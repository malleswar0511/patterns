def stack():
    stack=[]
    return stack

def empty_stack(stack):
    return len(stack)==0


def push(stack,item):
    stack.append(item)
    print("pushed item" + item)

def pop(stack):
    if(empty_stack(stack)):
        return "stack is empty"
    return stack.pop() 
stack=stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
print("popped item :" +  pop(stack))
print("stack after popping an element: " + str(stack))

