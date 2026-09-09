stack = []
size= int(input("Enter stack size:"))
n=int(input("Enter number of elements you want to push:"))
for i in range(n):
    if len(stack)<size:
       val=int(input("Enter value :"))
       stack.append(val)
    else:
        print("Stack over flow...")
while True:
    if len(stack)==0:
        print("Stack Empty ....!")
        break
    else:
        print("popped:",stack.pop())
        print("Latest Stack ",stack)