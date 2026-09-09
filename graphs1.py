vertices=['A','B','C','D']
n= int(input("Enter number of vertices"))
graph=[[0] * n for _ in range(n)]
print(graph)
edges= int(input("Enter number of edges:"))
print("Enter source: Destination: weight")
for i in range(edges):
    s,d,w=input().split()
    w= int(w)
    s= vertices.index(s)
    d=vertices.index(d)
    graph[s][d]= w
source= input("Enter source vertex:")
source= vertices.index(source)
Destination= intput("Enter Destination vertex: ")
source= vertices.index(source)
Destination= vertices.index(Destination)
distance= [100]*n
visited= [False]*n
parent= [-1]*n
for j in range(n):
    if not visited[j] and distance[j] < min_distance:
               min_distance= distance[j]
               current=j
    if current==-1:
        break
    visited[current]=True
    for i in range(n):
        if graph[current][j] !=0:
            new_distance= distance[current]+graph[current][j]
            if new_distance< distance[j]:
                distance[j]=new_distance
                parent[j]=current
path=[]
current- Destination
while current != -1:
    path.append(vertices[current])
    current= parent[current]
    path.reverse()
print("\nShortest path :")
print('->'.join(path))
print("Shortest distance:", distance[Destination])
