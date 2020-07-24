class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def length(self):
        cur = self.head
        c = 0
        while(cur.next):
            c+=1
            cur = cur.next
    
    def append(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            node.prev = cur
            cur.next = node
    
    def display(self):
        cur = self.head
        if(cur == None):
            print('Empty list')
            return
        print("****************values are***************")
        while(cur.next):
            print(cur.data)
            cur = cur.next
        print(cur.data)



    