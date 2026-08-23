class node:
    def __init__(self,data):
        self.data= data
        self.prev= None
        self.next= None
head = None
tail= None
n= int(input("Enter the size of DLL"))
for i in range(n):
    data = int(input("Enter value:"))
    newnode= node(data)
    if head is None:
        head=newnode
        tail=newnode
    else:
        newnode.next = head
        head.prev =newnode
        head = newnode
print("\n Forward traversal:")
temp= head
while temp is not None:
    print(temp.data, end="<->")
    temp= temp.next
print("Tail")
if head is None:
    print("DLL is Empty ")
    head= None
    tail= None
elif head.next  is None:
    head= None
    tail= None
else:
    tail= tail.prev
    tail.next= None
print("\n after deleting at end :")
temp= head
while temp is not None:
    print(temp.data, end="<->")
    temp= temp.next
print("Tail")
