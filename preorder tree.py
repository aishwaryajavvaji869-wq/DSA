#traversing a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
values=input("Enter elements:")
root=node(values[0])
queue=[root]
i=1
while i<len(values):
    current=queue.pop(0)
    if i<len(values):
        current.left=node(values[i])
        queue.append(current.left)
        i+=1
    if i<len(values):
        current.right=node(values[i])
        queue.append(current.right)
        i+=1
print("Tree created.....")     
def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right) 
preorder(root)