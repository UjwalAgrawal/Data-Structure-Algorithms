class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if(not self.head):
            self.head = Node(data)
        else:
            node = Node(data)
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = node
    
    def display(self):
        print("****************values are***************")
        cur = self.head
        while(cur.next):
            print(cur.data)
            cur= cur.next
        print(cur.data)


    def delete(self,num):
        cur = self.head
        while(cur.data!=num or not cur.next):
            


SinglyLL = LinkedList()
for _ in range(5):
    d = int(input())
    SinglyLL.append(d)

SinglyLL.display()



