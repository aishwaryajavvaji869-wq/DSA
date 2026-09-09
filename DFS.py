#DFS
from collections import deque
graph={'a':['b','c'],
       'b':['d','e'],
       'c':['f'],
       'd':[],
       'e':[],
       'f':[]
}
visited=set()
def dfs(vertex):
  visited.add(vertex)
  print(vertex,end=' ')
  for next_vertex in graph[vertex]:
    if next_vertex not in visited:
      dfs(next_vertex)
  return
start=input("enter starting node:")
dfs(start)