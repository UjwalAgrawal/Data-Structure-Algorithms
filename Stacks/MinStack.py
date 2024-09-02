class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.minEle = float('inf')

    def push(self, a):
        if not self.stack:
            self.stack.append(a)
            self.minEle = a
        elif (a >= self.minEle):
            self.stack.append(a)
        else:
            t = 2*a - self.minEle
            self.minEle = a
            self.stack.append(t)

    def pop(self):
        if not self.stack:
            return -1
        elif (self.stack[-1] < self.minEle):
            t = self.stack.pop()
            m = self.minEle
            self.minEle = 2 * self.minEle - t
            return m
        else:
            return self.stack.pop()

    def getMin(self):
        if not self.stack:
            return -1
        else:
            return self.minEle
    
    def top(self):
        if not self.stack:
            return -1
        elif self.stack[-1] >= self.minEle:
            return self.stack[-1]
        else:
            return self.minEle


s = Stack()
s.push(18)
s.push(19)
s.push(29)
s.push(15)
print(f"Current minimum element is: {s.getMin()}")
s.pop()
print(f"Top element is: {s.top()}")
print(f"Current minimum element is: {s.getMin()}")
s.push(16)
print(f"Current minimum element is: {s.getMin()}")
