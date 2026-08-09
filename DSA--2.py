# write a code to print reverse of a given number
n=int(input("Enter a number:"))
rev=0
while n>=0:
    d= n%10
    rev= rev*10+d
    n//=10
    print("reverse number",rev)