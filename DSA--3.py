#code to print the count of even digits and odd digits of a number
num=int(input("ENTER Number"))
even=0
odd=0
while num!=0:
    d=num%10
    if d%2==0:
        even+=1
    else:
        odd+=1
    num//=10
print("EVEN COUNT",even)
print("ODD COUNT",odd)
        

