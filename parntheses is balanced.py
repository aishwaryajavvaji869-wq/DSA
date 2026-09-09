s= input("Enter parentheses :")
stack=[]
for ch in s:
    if ch=='(' or ch=='[' or ch=='{':
       stack.append(ch)
    elif ch==')' or ch==']' or ch=='}':
        if not stack:
            print("Not balanced")
            break
        top=stack.pop()
        if (ch==')' and top!='(') or (ch==']' and top!='[') or (ch=='}' and top!='{'):
            print("Not balanced")
            break
else:
    if len(stack)==0:
        print(s,"Balanced")
    else:
        print(s,"Not Balanced")
    
