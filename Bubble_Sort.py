#sorting
#1.Bubble sort
#2.selection sort
#3.insertion sort
arr= list(map(int, input("Enter elements :").split()))
n=len(arr)
for i in range(n):
    for j in range(0,n-1-i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1]=arr[j+1],arr[j]
print(*arr)