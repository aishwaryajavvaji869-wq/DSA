#sliding winndow apporach
arr=list(map(int, input("Enter elements:").split()))
k= int(input("Enter slide size"))
window_sum= sum(arr[:k])
maximum= window_sum
for i in range(k, len(arr)):
    window_sum= window_sum+arr[i]-arr[i-k]
    if window_sum>maximum:
        maximum= window_sum
print(maximum)