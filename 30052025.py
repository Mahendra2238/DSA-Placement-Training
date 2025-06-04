# ['(',')'] and n value is given print no of permutations eg. n=2 "",(,),() o/p=4
# n=int(input())
# print(2**n+n%2)

# print max continuous increasing subsequence in a list and sum
# lt = [1, 2, 3, 4, 2, 7]
# max_len = 1
# curr_len = 1
# si = 0
# start = 0
# for i in range(1, len(lt)):
#     if lt[i] > lt[i - 1]:
#         curr_len += 1
#         if curr_len > max_len:
#             max_len = curr_len
#             si = start
#     else:
#         curr_len = 1
#         start = i
# print(lt[si:si + max_len])
# print(sum(lt[si:si + max_len]))

# Graphs
# simple graph - without loops
# Non simple graph - with loops
# An adjacency list is a space-efficient way to represent a graph where each node stores a list of its neighbors.
# graph = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0],
#     3: [1]
# }

# graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# d={}
# for i,j in graphs:
#     if i not in d:
#         d[i]=[j]
#     else:
#         d[i].append(j)
#     if j not in d:
#         d[j]=[i]
#     else:
#         d[j].append(i)
# print(d)

# print all paths
# from collections import defaultdict
# def all_paths(u,v,path=[]):
#     path.append(u)
#     if u==v:
#         print(path)
#         path.pop()
#         return
#     for i in d[u]:
#         if i not in path:
#             all_paths(i,v,path)
#     path.pop()
#     return
# graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# d=defaultdict(list)
# for i,j in graphs:
#     d[i].append(j)
#     d[j].append(i)
# print(d)
# print(all_paths(5,3))

# count 
# from collections import defaultdict
# def all_paths(u,v,path=set(),c=0):
#     path.add(u)
#     if u==v:
#         c+=1
#     else:
#         for i in d[u]:
#             if i not in path:
#                 c=all_paths(i,v,path,c)
#     path.remove(u)
#     return c
# graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# d=defaultdict(list)
# for i,j in graphs:
#     d[i].append(j)
#     d[j].append(i)
# print(d)
# print(all_paths(5,3))

# length of paths
# from collections import defaultdict
# def len_all_paths(u,v,path=[],c=0):
#     path.append(u)
#     if u==v:
#         print(path," -> ",c+1)        
#     else:
#         for i in d[u]:
#             if i not in path:
#                 c=c+1
#                 len_all_paths(i,v,path,c)
#                 c=c-1
#     path.pop()
#     return 
# graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# d=defaultdict(list)
# for i,j in graphs:
#     d[i].append(j)
#     d[j].append(i)
# print(d)
# print(len_all_paths(5,3))

# check if path exits or not
# from collections import defaultdict
# def check_if_path(u,v,path=[],c=0):
#     path.append(u)
#     if u==v:
#         return True        
#     else:
#         for i in d[u]:
#             if i not in path:
#                 if check_if_path(i,v,path,c):
#                     return True
#     path.pop()
#     return False
# graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# d=defaultdict(list)
# for i,j in graphs:
#     d[i].append(j)
#     d[j].append(i)
# print(d)
# print(check_if_path(5,3))

# bfs is efficient than dfn to check whether exist or not
# print all nodes in a graph using bfs
# import collections
# def print_all_nodes(u):
#     v={5} #set()
#     q=[u]
#     while q:
#         curr=q.pop()
#         print(curr)
#         for i in d[curr]:
#             if i not in v and i not in q:
#                 q.append(i)
#                 v.add(i)
#     # print(v)
# graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# d=collections.defaultdict(list)
# for i,j in graphs:
#     d[i].append(j)
#     d[j].append(i)
# print_all_nodes(5)

from collections import defaultdict
def print_all(u,v,path=[],cost=0):
    path.append(u)
    if u==v:
        print(path,cost)
    for i,w in d[u]:
        if i not in path:
            cost=cost+w
            print_all(i,v,path,cost)
            cost=cost-w
    path.pop()
    return
graph=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
d=defaultdict(list)
for i,j,w in graph:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
print_all(5,3)