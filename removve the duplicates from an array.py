#remove the duplicate elements from a sorted array
arr=list(map(int, input("Enter elemnets :").split()))
j=0
for i in range(1,len(arr)):
    if arr[i]!=arr[j]:
        arr[j]= arr[i]
print("array after remove duplicates", arr[:j+1])


#
slow=0
fast=0
for fast in range(1,len(arr)):
    if arr[fast] !=arr[slow]:
        slow+=1
        arr[slow]=arr[fast]
print(arr[:slow+1])