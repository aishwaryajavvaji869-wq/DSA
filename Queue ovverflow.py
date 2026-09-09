from queue import Queue
q= Queue()
q=Queue(maxsize=4)
print("=== Queue-Enqueue operation ===")
print("Enter elements - to finish enterif type stop")
print("Maximum size =",q.maxsize)
print("is the queue intially full",q.full())
while True:
    if q.full():
        print("Queue overflow....")
        print("current queue::",list(q.queue))
        break
    item= input("Enter elements to Enqueue:")
    if item.lower == 'stop':
        break
    q.put(item)
    print(f'{item} has been inserted in to Queue')
    print(f" Queue: {list(q.queue)}\n")
print("\n Final Queue", list(q.queue))
print("Total items:",q.qsize())
print("peek element:",q.queue[0])



while not q.empty():
    confirm= input("Press Enter to dequeue the element:")
    if confirm.lower()=="stop":
        break
    item=q.get()
    print("Dequeued:", item)
    print("\n Remaining Queue",list(q.queue))
if q.empty():
    print("Queue is empty...")
else:
    print("Final queue :",list(q.queue))