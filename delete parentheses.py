#delete the parenthese if not balanced
s= input("Enter parenthese :")
stack=[]
result=[]
for ch in s :
    if ch=='(':
        stack.append(len(result))
        result+=ch
    elif ch==')':
        if stack:
            stack.pop()
            result.append(ch)
        else:
            continue
for i in reversed(stack):
    result.pop(i)
print("".join(result))
        

        