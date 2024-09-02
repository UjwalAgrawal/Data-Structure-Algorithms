class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.supportStack = []

    def push(self, a):
        self.stack.append(a)
        if(not self.supportStack or self.supportStack[-1]>=a):
            self.supportStack.append(a)
    
    def pop(self):
        if len(self.stack) == 0:
            return -1
        t = self.stack.pop()
        if self.supportStack[-1] == t:
            self.supportStack.pop()
        return t
    
    def getMin(self):
        return self.supportStack[-1]

s = Stack()
s.push(18)
s.push(19)
s.push(29)
s.push(15)
print(f"Current minimum element is: {s.getMin()}")
s.pop()
print(f"Current minimum element is: {s.getMin()}")
s.push(16)
print(f"Current minimum element is: {s.getMin()}")
