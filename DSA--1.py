# write a code to print the sum of digits of a given number.
n=int(input("Enter a number:"))
sum=0
while n!=0:
    d= n%10
    sum+=d
    n//=10
    print("Sum of digits",sum)