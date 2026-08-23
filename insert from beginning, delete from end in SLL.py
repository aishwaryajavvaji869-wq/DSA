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
    
print("SLL before deletion :")
temp= head
while temp is not None:
    print(temp.data, end='->')
    temp= temp.next
print("Tail")

if head is None:
    print("SLL Empty")
elif head.next is None:
    head= None
else:
    temp= head
    while temp.next.next is not None:
        temp= temp.next
print("Tail")

print("SLL after deletion :")
temp= head
while temp is not None:
    print(temp.data, end='->')
    temp= temp.next
print("Tail")