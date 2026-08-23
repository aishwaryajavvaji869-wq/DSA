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

prev= None
curr= head
while curr is not None:
    next_node= curr.next
    curr.next= prev
    prev = curr
    curr= next_node
head= prev


print("Linked list after reverse :")
temp = head
while temp is not None:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
