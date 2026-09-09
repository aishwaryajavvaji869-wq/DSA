stack1 = []
stack2 = []
merged = []
n1= int(input("Enter number of elements in stack 1: "))
for i in range(n1):
    val= int(input("Enter value : "))
    stack1.append(val)
n2 = int(input("Enter number of elements in stack 2: "))
for i in range(n2):
    val= int(input("Enter value : "))
    stack2.append(val)
for i in range(len(stack1)):
    merged.append(stack1[i])
    merged.append(stack2[i])
for i in range(len(stack1)):
    print(stack1[i], end= ' ')
    print(stack2[i], end= ' ')
print("Merged stack : ",merged)