n=int(input("Enter a value:"))
for i in range (n):
    for j in range(n):
        if (i+j)==n-1 or j==n or i==n-1 or j==n-1:
           print("*",end=' ')
        else:
             print(' ',end=' ')
    print()