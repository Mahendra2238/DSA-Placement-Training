class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
# insert nodes
def insert(root,x):
    if root==None:
        return Node(x)
    if x<root.data:
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
# count leafnodes using dfs traversal
def count_leafnodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    return count_leafnodes(root.left)+count_leafnodes(root.right)
# print paths from root to leaf
def paths_R2L(root,p):
    if root==None:
        return
    p.append(root.data)#p=p+"->"+str(root.data)
    if root.left==None and root.right==None:
        print(p)
        p.pop()
        return
    paths_R2L(root.left,p)
    paths_R2L(root.right,p)
    p.pop()
# bfs level order traversal
def level(root,l):
    if root==None:
        return
    l.append(root)
    while l:
        curr=l.pop(0)
        if curr.left!=None:
            l.append(curr.left)
        if curr.right!=None:
            l.append(curr.right)
        print(curr.data,end=" ")
# count leaf nodes using level order traversal
def lcount(root,l):
    if root==None:
        return
    l.append(root)
    c=0
    while l:
        curr=l.pop(0)
        if curr.left==None and curr.right==None:
            c=c+1
        if curr.left!=None :
            l.append(curr.left)
        if curr.right!=None:
            l.append(curr.right)
    print(c)
def leftview(root,d={},c=0):
    if root==None:
        return
    if c not in d:
        d[c]=root.data
    leftview(root.left,d,c+1)
    leftview(root.right,d,c+1)
    return d
def rightview(root,d={},c=0):
    if root==None:
        return
    d[c]=root.data
    rightview(root.left,d,c+1)
    rightview(root.right,d,c+1)
    return d
def topview(root): 
    d={}
    c=0
    l=[(root,0)]
    while(l):
        curr,c=l.pop(0)
        if c not in d:
            d[c]=curr.data
        if curr.left!=None:
            l.append((curr.left,c-1))
        if curr.right!=None:
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
    # if root==None:
    #     return
    # l.append([root,0])
    # while l:
    #     curr=l.pop(0)
    #     if curr[0].left!=None:
    #         l.append([curr[0].left,curr[1]-1])
    #     if curr[0].right!=None:
    #         l.append([curr[0].right,curr[1]+1])
    #     if curr[1] not in d:
    #         d[curr[1]]=curr[0].data
    # print(sorted(d.values()))
def bottomview(root):  #vertical
    d={}
    c=0
    l=[(root,0)]
    while(l):
        curr,c=l.pop(0)
        d[c]=curr.data
        if curr.left!=None:
            l.append((curr.left,c-1))
        if curr.right!=None:
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
# lowest common ancestor
def lca(root,a,b): #,p=[]
# for binary search tree
    # if root==None:
    #     return
    # if a<root.data and b<root.data:
    #     return lca(root.left,a,b)
    # if a>root.data and b>root.data:
    #     return lca(root.right,a,b)
    # return root.data
#for binary tree
    if root==None:
        return 
    # p.append(root.data)
    if root.data==a or root.data==b:
        # print(p)
        # p.pop()
        return root
    l=lca(root.left,a,b) #,p)
    r=lca(root.right,a,b) #,p)
    # p.pop()
    if l!=r!=None :
        return root.data
    if l!=None:
        return l
    else:
        return r
# balanced or not 
def height(root):
    if root==None:
        return-1
    return max(height(root.left),height(root.right))+1
def baltree(root):
    if root==None:
        return True
    l=height(root.left)
    r=height(root.right)
    if abs(l-r)>1:
        return False
    return baltree(root.left) and baltree(root.right)
root=None
root=insert(root,10)
root=insert(root,5)
root=insert(root,2)
root=insert(root,20)
root=insert(root,8)
root=insert(root,18)
root=insert(root,22)
# inorder(root)
# print()
# print(count_leafnodes(root))
# print(paths_R2L(root,p=[]))
# level(root,l=[])
# lcount(root,l=[])
# print(leftview(root))
# print(rightview(root))
# topview(root)
# print()
# bottomview(root)
# print()
# print(lca(root,2,8))
print(baltree(root))
# horizantal(-) and vertical(|) levels tree to print top view/outer nodes 
# -2  -1  0  1  2
#         10
#     5      2 0
# 2      8,11   22