# number of provinces
# def n_prov(i):
#     l[i]=True
#     for j in range(n):
#         if isCon[i][j]==1 and i!=j and l[j]!=True:   
#             n_prov(j)
# isCon = [[1,0,0],[0,1,0],[0,0,1]]
# n=len(isCon)
# l=[False]*n
# c=0
# for i in range(n):
#     if l[i]==False:
#         c+=1
#         n_prov(i)
# print(c)

# Dijkstra's algorithm
# won't work for negative weightage
# we get single source shortest path
from collections import defaultdict
import heapq
# def dijkstra(): 
#     while heap:
#         c,u=heapq.heappop(heap)
#         for v,w in d[u]:
#             if v not in rd or c+w<rd[v]:
#                 rd[v]=c+w
#                 heapq.heappush(heap,(rd[v],v))
#     return rd
# g=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(7,8,1),(7,5,1),(8,3,1)]
# d=defaultdict(list)
# for i,j,w in g:
#     d[i].append([j,w])
# rd=defaultdict(int)
# for i,j,w in g:
#     rd[i]=float('inf')
# st=g[0][0]
# rd[st]=0
# heap=[(0,st)]
# print(heap)
# print(d)
# print(rd)
# print(dijkstra())

# sir
# def sssp(u,v):
#     sp=defaultdict(int)
#     dis=defaultdict(lambda:float('inf'))
#     sp[u]=0
#     dis[u]=0
#     q=[u]
#     vi=set()
#     while q:
#         n=q.pop()
#         vi.add(n)
#         for i,w in d[n]:
#             if dis[n]+w<dis[i]:
#                 dis[i]=dis[n]+w
#                 sp[i]=n
#             if i not in q and i not in vi:
#                 q.append(i)
#     print(dis)
#     l=[v]
#     while sp[v]!=v:
#         l.append(sp[v])
#         v=sp[v]
#     print(l[::-1])
# g=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(7,8,1),(7,5,1),(8,3,1)]
# d=defaultdict(list)
# for i,j,w in g:
#     d[i].append([j,w])
# sssp(10,3)

# prims using bfs     min spanning tree(connected all nodes without cycles)
import heapq
def prims(u):
     vi=set()
     tc=0
     path=[]
     q=[(0,u)]
     while q:
        #   print(q,vi)
          cost,u=heapq.heappop(q)         
          if u in vi:
              continue
          tc+=cost
          path.append(u)
          vi.add(u) 
          for v,w in d[u]:
               if v not in vi:
                    heapq.heappush(q,(w,v))
     print(*path)
     print(tc)
g=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(7,8,1),(7,5,1),(8,3,1)]
d=defaultdict(list)
for i,j,w in g:
    d[i].append([j,w])
# print(d)
prims(10)
# print(len(d.keys()))
