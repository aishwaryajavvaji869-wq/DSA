#competitive coding
#pancake sort/flip sort
def flip(arr,k):
    arr[:k+1]=arr[:k+1][::-1]
def pancakesort(arr):
    n=len(arr)
    for size in range(n,1,-1):
        max_index= arr.index(max(arr[:size]))
        if max_index !=size-1:
            if max_index !=0:
                flip(arr,max_index)
            flip(arr,size-1)
n=int(input("enter array size:"))
arr= list(map(int,input("Enter elements").split()))
pancakesort(arr)
print("Sorted array:",*arr)