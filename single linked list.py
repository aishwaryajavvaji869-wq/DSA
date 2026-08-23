class node:
    def __init__(self,data):
        self.data= data
        self.next= None
head= None
n= int(input("Enter number of nodes: "))
for i in range(n):
    data= int(input("Enter data : "))
    newnode= node(data)
    if head is None:
        head= newnode
    else:
        temp= head
        while temp.next is not None:
            temp= temp.next
        temp.next= newnode
print("SLL:")
temp= head
while temp is not None:
    print(temp.data, end='->')
    temp= temp.next
print("Tail")