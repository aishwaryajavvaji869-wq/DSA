#traverse the matrix in a spiral order and print the path
n= int(input("Enter the size :"))
r= int(input("Enter number of rows:"))
c= int(input("Enter number of cols:"))
a=[]
print("Enter matrix elements")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    a.append(row)
top= 0
bottom=r-1
left= 0
right=c-1
num=1
while top<=bottom and left<=right:
    #traverse at top from left to right
    for i in range(left,right+1):
        print(a[top][i], end=' ')
        num+=1
    top+=1
    #traverse at right from top->bottom
    for i in range(top, bottom+1):
        print(a[i][right], end=' ')
        num+=1
    right-=1
    #traverse at bottom from right-> left
    for i in range(right, left-1,-1):
        print(a[bottom][i],end=' ')
        num+=1
    bottom-=1
    #traverse at left from bottoom-> top
    for i in range(bottom, top-1,-1):
        print(a[i][left],end=' ')
        num+=1
    left+=1
for row in a:
    for val in row:
        print(f"{val:3}", end=' ')
    print()