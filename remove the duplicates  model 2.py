arr=list(map(int, input("Enter elemnets :").split()))
slow=0
fast=0
for fast in range(1,len(arr)):
    if arr[fast] !=arr[slow]:
        slow+=1
        arr[slow]=arr[fast]
print(arr[:slow+1])