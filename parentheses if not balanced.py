#adding the parenthese if not balanced
s= input("Enter parenthese :")
stack=[]
result=""
for ch in s :
    if ch=='(':
        stack.append(ch)
        result+=ch
    elif ch==')':
        if stack:
            stack.pop()
            result+=ch
        else:
            result='('+result+ch
while stack:
    result+=')'
    stack.pop()
print(result)
            

        