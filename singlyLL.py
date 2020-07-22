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
            pass

    def length(self):
        count = 0
        cur = self.head
        while(cur.next):
            count+=1
            cur = cur.next
        return(count+1)

    def insert(self, data, pos):
        l = self.length()
        self.pos = pos
        cur = self.head
        node = Node(data)
        if(self.pos>=l):
            while(cur.next):
                cur = cur.next
            cur.next = node
            print("Data inserted at the end")
        else:
            self.pos-=1
            while(self.pos):
                cur = cur.next
                self.pos-=1
            node.next = cur.next
            cur.next = node
           


SinglyLL = LinkedList()
for _ in range(5):
    d = int(input())
    SinglyLL.append(d)

SinglyLL.display()
SinglyLL.insert(100,3)
SinglyLL.display()



