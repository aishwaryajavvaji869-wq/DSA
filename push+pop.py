import heapq
heap=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    value= int(input("Enter element:"))
    heapq.heappush(heap,value)
print("min heap", heap)
x=int(input("Enter a value to push"))
removed=heapq.heappushpop(heap,x)
print("Removed element:", removed)
print("min heap",heap)