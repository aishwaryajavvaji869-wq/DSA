#parentheses are balanced or not
s= input("Enter parenthese:")
stack=[]
for ch in s :
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if len(stack)==0:
            print('Notbalanced')
            break
        stack.pop()
else:
    if len(stack)==0:
        print("balanced")
    else:
        print("not balanced")