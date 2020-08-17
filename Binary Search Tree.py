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
        print("\nThe values in inorder are:", end= " ")
        self.inlist = []
        self.__inOrder(self.root)
        print(self.inlist)

    def __inOrder(self,root):
        if(root):
            self.__inOrder(root.left)
            self.inlist.append(root.value)
            self.__inOrder(root.right)

    def preOrder(self):
        print("\nThe values in preorder are:", end= " ")
        self.prelist = []
        self.__preOrder(self.root)
        print(self.prelist)

    def __preOrder(self, root):
        if(root!=None):
            self.prelist.append(root.value)
            self.__preOrder(root.left)
            self.__preOrder(root.right)

    def postOrder(self):
        print("\nThe values in postorder are:", end= " ")
        self.postlist = []
        self.__postOrder(self.root)
        print(self.postlist)

    def __postOrder(self, root):
        if(root!=None):
            self.__postOrder(root.left)
            self.__postOrder(root.right)
            self.postlist.append(root.value)
    
    def levelOrder(self):
        h = self.height()
        print("\nThe values in levelOrder are:", end= " ")
        for i in range(1,h+2):
            self.printgivenlevel(self.root,i)


    def printgivenlevel(self,root,h):
        if(root==None):return
        if h==1:
            print(root.value,end=" ")
        elif(h>1):
            self.printgivenlevel(root.left,h-1)
            self.printgivenlevel(root.right,h-1)
    
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
    
    def height(self):
        return(self.__height(self.root))
    
    def __height(self, t, h=-1):
        if(t==None):
            return(h)
        lh = self.__height(t.left, h+1)
        rh = self.__height(t.right, h+1)
        return(max(lh, rh))


        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.add(arr[i])

tree.preOrder()
tree.postOrder()
tree.inOrder()
tree.levelOrder()
tree.search(int(input("\nWhich number you want to search: ")))
print(f"Height of the tree is {tree.height()}")