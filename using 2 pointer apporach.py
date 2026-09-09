#find the pair with given sum using 2 pointer appoarach
arr= list(map(int, input("Enter elements ").split()))
target= int(input("Enter target:"))
left= 0
right= len(arr)-1
found = False
while left<right:
    total= arr[left]+arr[right]
    if total==target:
        print("pair found values", arr[left],arr[right])
        print("pair found index:",left,right)
        found= True
        break
    elif total<target:
        left+=1
    else:
        right-=1
if not found:
    print("No pair found")
            
            