#insert at poistion
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head= None
n= int(input("Enter the size of SLL:"))
for i in range(n):
    data= int(input("Enter Value:"))
    newnode= node(data)
    if head is None:
        head= newnode
    else:
        temp= head
        while temp.next is not None:
            temp=temp.next
        temp.next= newnode
print("Linked list after insertion :")
temp = head
while temp is not None:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")

data=int(input("\n Enter data to insert:"))
poistion= int(input("\n Enter poistion of data :"))
newnode= node(data)
if poistion==1:
    newnode.next = head
    head = newnode
else:
    temp = head
    for i in range(poistion-2):
        temp= temp.next
    newnode.next= newnode
    
print("Linked list after poistion insertion :")
temp = head
while temp is not None:
    print(temp.data,end='->')
    temp= temp.next
print("Tail")
        
    