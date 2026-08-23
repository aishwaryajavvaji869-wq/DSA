#Circular LL
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head=None
n=int(input("Enter no.of nodes: "))
for i in range(n):
    data = int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head = newnode
        newnode.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = newnode
        newnode.next = head
#Display Original linked list
print("\n Circular Linked List: ")
temp = head
while True:
    print(temp.data,end=' ')
    temp = temp.next
    if temp==head:
        break
#getting start value
start = int(input("\nEnter the node u want to start: "))
#finding start node
temp = head
startnode = None
while True:
    if temp.data == start:
        startnode = temp
        break
    temp = temp.next
    if temp==head:
        break

#traverse and print from start node
if startnode is None:
    print("Start node not found ...")
else:
    print("Traversal for", start, ":")
    temp = startnode
    while True:
        print(temp.data,end=" ")
        temp = temp.next
        if temp==startnode:
            break