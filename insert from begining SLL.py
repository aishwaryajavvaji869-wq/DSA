class node:
    def __init__(self,data):
        self.data= data
        self.next= None
head= None
n= int(input("Enter number of nodes: "))
for i in range(n):
    data= int(input("Enter data : "))
    newnode= node(data)
    newnode.next = head
    head= newnode
    
print("SLL:")
temp= head
while temp is not None:
    print(temp.data, end='->')
    temp= temp.next
print("Tail")