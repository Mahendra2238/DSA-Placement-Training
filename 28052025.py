# stacks
# prefix,infix,postfix
# The reason for converting infix to postfix or prefix is to solve and evaluate a expression by comp
# a+b*c-e infix
# -+a*bce prefix
# abc*+e- postfix

# Infix: (a + b * c) / e - i * (j - e)
# Prefix: - / + a * b c e * i - j e
# Postfix: a b c * + e / i j e - * -

# 523*+4-
# every time when operator comes pop 2 ele from stack and push result and final top of the stack is the result
# s=> 
# 5 2 3
# 5 6
# 11 4
# 6

# evaluate
# a="15,-13,+,6,2,-,*"
# a=a.split(',')
# # opt="+-*/"
# # opt=set(opt)
# s=[]
# for i in a:
#     if i[-1].isdigit():
#         s.append(int(i))
#     else: #i in opt:
#         b=s.pop()
#         a=s.pop()
#         op=i
#         if op=='+':
#             r=a+b
#         elif op=='-':
#             r=a-b
#         elif op=='*':
#             r=a*b
#         elif op=='/':
#             r=a/b
#         else:
#             r=a**b
#         s.append(r)
# print(s[-1])

# valid paranthesis
# a="([{}])"
# s=[]
# for i in range(len(a)):
#     if a[i] in {'(','[','{'}:  #very minute change to use set to reduce t.c
#         s.append(a[i])
#     elif s:
#         if a[i]=='}' and s[-1]=='{': # u can use dict also
#             s.pop()
#         elif a[i]==')' and s[-1]=='(':
#             s.pop()
#         elif a[i]==']' and s[-1]=='[':
#             s.pop()
#         else:
#             print("iv") #invalid
#             break
#     else:  # stack empty
#         print("iv")
#         break
# else:
#     if s:
#         print("iv")
#     else:
#         print("valid")

# a="([{}])"
# s=[]
# d={'}':'{',']':'[',')':'('}
# for i in range(len(a)):
#     if a[i] in {'(','[','{'}: 
#         s.append(a[i])
#     else:
#         if s and d[a[i]]==s[-1]:
#             s.pop()
#         else:
#             print("iv")
#             break
# else:
#     if s:
#         print("invalid")
#     else:
#         print("valid")

# o(n*m) not efficient
# i1=[4,1,2]
# i2=[2,1,3,4]
# res=[]
# for i in range(len(i1)):
#     for j in range(len(i2)):
#         if i1[i]==i2[j]:
#             k=j
#             f=0
#             while k<len(i2):
#                 if i2[k]>i1[i]:
#                     res.append(i2[k])
#                     f=1
#                     break
#                 k+=1           
#             if not f:
#                 res.append(-1)
#             break
# print(res)

# o(2n) or o(n+m)
# i1 = [4, 1, 2]
# i2 = [2, 1, 3, 4]
# next_greater = {}
# stack = []
# for num in reversed(i2):
#     while stack and stack[-1] <= num:
#         stack.pop()
#     next_greater[num] = stack[-1] if stack else -1
#     stack.append(num)
# res = [next_greater[num] for num in i1]
# print(res)

# Trees
'''
Binary trees -> Each node has upto 2 child nodes
Full binary tree(proper bt) -> the inner nodes can have either 0 or 2 child nodes
Perfect bt-> if both left and right have 2 nodes
Complete bt-> all leaf nodes should be same level, all nodes are filled from left to right (left heavy tree/leaning towards left side)   
All perfect bt are complete but not all full bt are complete bt
For both perfect and complete bt leaf nodes are at same level
Balance bt -> balance of any node in the tree is 0,1
Bal=|Lh-Rh| (height of left sub tree - height of right sub tree)
if root=None return -1
Height of bt is the no of edges crossed from leaf node to root node (height of leafnode is 0 and depth of root node is 0) 
Avl tree is a balanced tree (all nodes) (Adelson-Velsky and Landis Tree)
Binary search tree -> left side should be less and right side should be greater
left < root < right.
Arrange and store data in such a way such that u can retrieve it easily (search time is reduced) - ll,trees..
For bst in worst case it can be o(n) not o(logn) so it should be balanced (eg. 7,8,9,10,11,12,13,14 where root node is 8)
Diff b/w bst and bal bt ->Bst it is not required to be balanced. In bst it should be balanced
when tree is avl and bst, t.c is o(logn)

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    def preorder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
    # sum of all nodes
    def sum_all(self,root):
        if root==None:
            return 0
        return root.data+self.sum_all(root.left)+self.sum_all(root.right)
    # sum even no
    def even_sum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.even_sum(root.left)+self.even_sum(root.right)
        else:
            return self.even_sum(root.left)+self.even_sum(root.right)    
    # height
    def height(self,root):
        if root==None:
            return-1
        return max(self.height(root.left),self.height(root.right))+1
    # binary search when root and search key is given
    def bin(self,root,key):
        if root==None:
            return None
        if root.data==key:
            return root.data
        elif key<root.data:
            return self.bin(root.left,key)
        else:
            return self.bin(root.right,key)
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(22)
# root.inorder(root)
# print()
# root.preorder(root)
# print()
# root.postorder(root)
# print()
# print(root.sum_all(root))            
# print(root.even_sum(root))
# print(root.height(root))
print(root.bin(root,20))