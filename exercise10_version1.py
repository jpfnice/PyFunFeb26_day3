"""
Write a Stack class using a composition mechanism (the Stack class will use internally the List class).
The Stack class should offer the following facilities:
    a push() method to add an element on top of the Stack
    a pop() method to get and remove the element on top of the Stack
    a peek() method to get the element on top of the Stack
    a way to determine its size (its current number of elements),
    a way to print easily the content of the Stack
    a way to test if an element belongs to the stack or not
    
Name of the method to provide:
    
    push(self,element) -> None
    pop(self) -> element
    peek(self) -> element
    __len__(self) -> int
    __repr__(self) -> str
    __contains__(self, element) -> bool
    __init__(self,mSize) -> None
    
Name of the attributes to provide:
    maxSize -> int
    content -> list
    
"""
class Stack:
    def push(self, element):
        if len(self) < self.maxSize:
            self.content.append(element)
        else:
            raise Exception("The maximum size is reached !!")
    def pop(self):
        if len(self) > 0:
            return self.content.pop()
        else:
            raise Exception("The Stack is empty !!")
    def peek(self) :
        if len(self) > 0:
            return self.content[-1]
        else:
            raise Exception("The Stack is empty !!")
    def __len__(self) :
        return len(self.content)
    def __repr__(self) : # (3/12) [10,8,67]
        return f"({len(self)}/{self.maxSize}) {self.content}"
    def  __contains__(self, element) :
        return element in self.content
    def __init__(self, msize) :
        if isinstance(msize, int) and msize > 0:
            self.maxSize=msize
        else:
            raise Exception("Wrong size given!")
        self.content=[] # <=> self.content=list()
        
    
s1=Stack(12) # 12 is the maxmimum size of the Stack s1
s1.push(10)
s1.push(8)
s1.push(67)
print(s1) # (3/12) [10,8,67]
print("Size of the stack", len(s1)) # Size of the stack 3
top=s1.pop()
print(s1) # (2/12) [10,8]
print("Size of the stack", len(s1)) # Size of the stack 2
print(top) # 67
top=s1.peek()
print(s1) # (2/12) [10,8]
print("Size of the stack", len(s1)) # Size of the stack 2
print(top) # 8