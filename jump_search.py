#jump search
import math
arr= list(map(int, input("Enter elements :").split()))
key= int(input("Enter a target:"))
n= len(arr)-1
step= int(math.sqrt(n))
prev= 0
found= False
while prev<n and arr[min(step,n)-1]<key:
    prev= step
    step+=int(math.sqrt(n))
    if prev>=n:
        break
while prev<min(step,n):
    if arr[prev]==key:
        print("Element found at",prev)
        found= True
        break
    prev+=1
if not found:
    print("Element not found")