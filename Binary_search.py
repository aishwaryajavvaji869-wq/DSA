#2.Binary search
arr=list(map(int,input("Enter elements:").split()))
target= int(input("Enter a target:"))
left= 0
right= len(arr)-1
found = False
while left<= right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(target," found at index",mid)
        found= True
        break
    elif target < arr[mid]:
        right= mid-1
    else:
        left= mid+1
if not found :
    print("Element doesnt exist ")
       