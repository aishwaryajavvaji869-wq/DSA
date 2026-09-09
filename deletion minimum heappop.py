import heapq
heap=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    value= int(input("Enter element:"))
    heapq.heappush(heap,value)
print("min heap", heap)
deleted= heapq.heappop(heap)
print("Deleted element:", deleted)
print("min heap",heap)