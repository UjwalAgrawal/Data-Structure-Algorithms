class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    if(root):
        res = [root.info]
        queue = [(root, 0)]
        mini = 0
        maxi = 0
        while queue:
            node, pos = queue.pop(0)
            if(pos < mini):
                res.insert(0, node.info)
                mini = pos
            if(pos > maxi):
                res.append(node.info)
                maxi = pos
            if(node.left):            
                queue.append((node.left, pos - 1))
            if(node.right):
                queue.append((node.right, pos + 1))
        print("The top view is:",*res)  
    else:
        print([])          
            

tree = BinarySearchTree()
t = int(input("Please enter number of nodes: "))

arr = list(map(int, input("Please enter the nodes\n").split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)