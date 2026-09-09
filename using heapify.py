import heapq
heap=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    value= int(input("Enter element:"))
    heap.append(value)
print("min heap", heap)
heapq.heapify(heap)
print("min heap",heap)