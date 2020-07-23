class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
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
        cur = self.head
        if(cur==None):
            print('Empty list')
            return
        print("****************values are***************")
        while(cur.next):
            print(cur.data)
            cur= cur.next
        print(cur.data)


    def delete(self,num):
        cur = self.head
        prev = self.head
        while(cur.next):
            if(cur.data==num):
                prev.next = cur.next
                print(f"\n{num}, deleted successfully!!!")
                break
            else:
                prev = cur
                cur = cur.next
        if(cur.data==num):
            prev.next = None
        self.display()
        


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
           


my_list = SinglyLL()
"""for _ in range(5):
    d = int(input())
    my_list.append(d)"""

my_list.display()
my_list.insert(100,3)
my_list.display()
my_list.delete(5)



