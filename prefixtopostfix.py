#prefix to postfix
def prefixtopostfix(expression):
    stack=[]
    for ch in expression[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            operand1= stack.pop()
            operand2= stack.pop()
            result= operand1+operand2+ch
            stack.append(result)
    return stack.pop()
expression=input("Enter expression:")
postfix=prefixtopostfix(expression)
print(postfix)