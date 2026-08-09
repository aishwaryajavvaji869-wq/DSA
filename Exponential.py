def abc(n):
    if n==0:
        return
    print(n)
    abc(n-1)
    abc(n-1)
n=int(input("Enter a number :"))
abc(n)