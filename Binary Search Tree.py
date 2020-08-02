class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if(not self.root):
            self.root = Node(value)
        else:
            cur = self.root
            while(True):
                if(value < cur.value):
                    if(cur.left):
                        cur = cur.left
                    else:
                        cur.left = Node(value)
                        break
                elif(value > cur.value):
                    if(cur.right):
                        cur = cur.right
                    else:
                        cur.right = Node(value)
                else:
                    break
    def inOrder(self):
        print("\nThe values in preorder are:", end= " ")
        self.__inOrder(self.root)

    def __inOrder(self,root):
        if(root):
            self.__inOrder(root.left)
            print(root.value,end=" ")
            self.__inOrder(root.right)

    def preOrder(self):
        print("\nThe values in preorder are:", end= " ")
        self.__preOrder(self.root)

    def __preOrder(self, root):
        if(root!=None):
            print(root.value,end=" ")
            self.__preOrder(root.left)
            self.__preOrder(root.right)

    def postOrder(self):
        print("\nThe values in postorder are:", end= " ")
        self.__postOrder(self.root)

    def __postOrder(self, root):
        if(root!=None):
            self.__postOrder(root.left)
            self.__postOrder(root.right)
            print(root.value,end=" ")
    
    def search(self, num):
        self.__search(self.root, num)

    def __search(self, t, num):
        if(t==None):
            print("Not present")
            return
        elif(num == t.value):
            print("Present")
            return
        elif(num > t.value):
            self.__search(t.right, num)
        else:
            self.__search(t.left, num)

        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.add(arr[i])

tree.preOrder()
tree.postOrder()
tree.inOrder()
tree.search(int(input("\nWhich number you want to search: ")))