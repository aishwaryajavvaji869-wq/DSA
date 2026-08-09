#searching types
#linear search
#binary search
#jump search
arr = list(map(int, input("Enter elements : ").split()))
target= int(input("Enter a target:"))
for i in range(len(arr)):
    if arr[i]==target:
        print(target,"Found at index: ",i)
        break