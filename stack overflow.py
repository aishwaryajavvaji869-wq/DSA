stack = []
size= int(input("Enter stack size:"))
n=int(input("Enter number of elements you want to push:"))
for i in range(n):
    if len(stack)<size:
       val=int(input("Enter value :"))
       stack.append(val)
    else:
        print("Stack over flow...")
print("Stack: ",stack)
print("Satck :",stack[-1])
print("Removed from stack: ", stack.pop())
print("Stack:",stack)
print("peek element :",stack[-1])
