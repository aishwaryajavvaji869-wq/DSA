#Create a undirected graph-adjaceny matrix
n=int(input("Enter number of vertices : "))
vertices=[]
print("Enter vertices : ")
for i in range(n):
  vertices.append(input().upper())
graph=[[0] * n for i in range(n)]
edge=int(input("enter number of edges : "))
print("Enter edges : ")
for i in range(edge):
  e,v=input().upper().split()
  x=vertices.index(e)
  y=vertices.index(v)
  graph[x][y]=1
  graph[y][x]=1
print("\n graph created...")
print("\n adjaceny matrix : ")
print(" ")
for v in vertices:
  print(v,end=" ")
print()
for i in range(n):
  print(vertices[i],end=' ')
  for j in range(n):
    print(graph[i][j],end=' ')
  print()