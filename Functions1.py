#arg pass no return value
def summate(n1,n2):
    print("Sum:", n1+n2)
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
summate(n1,n2)



#no args but returns value
def summate():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    return n1+n2
result= summate()
print("Sum:", result)


#no arg no return
def summate():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    print("Sum:",n1+n2)
summate()

    