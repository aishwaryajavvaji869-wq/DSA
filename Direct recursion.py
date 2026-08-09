#Direct Recursion
#code to print n natural numbers using direct recursion
def numbers(n):
    if n==0:
        return
    print(n, end=' ')
    numbers(n-1)
n=int(input("Enter a number:"))
numbers(n)