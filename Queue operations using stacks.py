#implementations of queue operations using stacks
stack1=[]
stack2=[]
def enqueue(val):
    stack1.append(val)
def dequeue():
    if len(stack1)==0:
        print("Queue underflow ....")
    else:
        while stack1:
            stack2.append(stack1.pop())
        print("Removed :",stack2.pop())
        while stack2:
            stack1.append(stack2.pop())
n=int(input("Enter number of elements:"))
for i in range(n):
    val= int(input("Enter value :"))
    enqueue(val)
print("Queue",stack1)
dequeue()
