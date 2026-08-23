#Binary search variations
#1.Find a square root of a number using binary search pattern
n= int(input("Enter a value:"))
left = 0
right = n
ans= 0
while left<= right :
    mid= (left+right)//2
    if mid*mid==n:
        ans=mid
        break
    elif mid*mid<n:
        ans= mid
        left= mid+1
    else:
        right= mid-1
print("square root:",ans)