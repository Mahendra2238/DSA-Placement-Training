# merge two sorted lists into one 

# def merge(a,b):
#     c=[] #[0]*(len(a)+len(b))
#     i=j=0
#     # k=0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             c.append(a[i])  #c[k]=a[i]
#             i+=1
#         else:
#             c.append(b[j]) #c[k]=b[j]
#             j+=1
#         # k+=1
#     while i<len(a):
#         c.append(a[i]) #c[k]=a[i]
#         i+=1
#         # k+=1
#     while j<len(b):
#         c.append(b[j]) #c[k]=b[j]
#         j+=1
#         # k+=1
#     return c
# a=[2,4,5,8,9]
# b=[3,5,6,9,11,12,13]
# print(merge(a,b))

# def mergesort(a, l, h):
#     if l < h:
#         mid = (l + h) // 2
#         mergesort(a, l, mid)
#         mergesort(a, mid + 1, h)
#         merge(a, l, mid, h)
# def merge(a, l, mid, h):
#     temp = [0] * (h - l + 1)  # temporary array
#     i, j = l, mid + 1
#     k = 0
#     while i <= mid and j <= h:
#         if a[i] < a[j]:
#             temp[k] = a[i]
#             i += 1
#         else:
#             temp[k] = a[j]
#             j += 1
#         k += 1
#     while i <= mid:
#         temp[k] = a[i]
#         i += 1
#         k += 1

#     while j <= h:
#         temp[k] = a[j]
#         j += 1
#         k += 1
#     for i in range(len(temp)):
#         a[l + i] = temp[i]
# a = [3, 5, 6, 9, 11, 12, 13]
# mergesort(a, 0, len(a) - 1)
# print(a)

# def merge_sort(x):
#     if len(x)==1:
#         return x
#     m=len(x)//2 
#     l=merge_sort(x[:m])
#     r=merge_sort(x[m:])
#     return merge(l,r)
# def merge(a,b):
#     c=[] 
#     i=j=0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             c.append(a[i])
#             i+=1
#         else:
#             c.append(b[j]) 
#             j+=1
#     while i<len(a):
#         c.append(a[i])
#         i+=1
#     while j<len(b):
#         c.append(b[j]) 
#         j+=1
#     return c
# a = [3, 5, 6, 9, 11, 12, 13]
# print(merge_sort(a))

# kth largest number
# def merge_sort(x):
#     if len(x)==1:
#         return x
#     m=len(x)//2 
#     l=merge_sort(x[:m])
#     r=merge_sort(x[m:])
#     return merge(l,r)
# def merge(a,b):
#     c=[] 
#     i=j=0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             c.append(a[i])
#             i+=1
#         else:
#             c.append(b[j]) 
#             j+=1
#     while i<len(a):
#         c.append(a[i])
#         i+=1
#     while j<len(b):
#         c.append(b[j]) 
#         j+=1
#     return c
# def klargest(a,k):
#     merge_sort(a)
    # a=list(set(a))
    # print(a[len(a)-k])
# a=[2,13,4,2,9,9,5,8,7,7,13,3]
# k=3
# klargest(a,k)     

# kth largest frequency
# def bucketsort(ip,k):
#     d={}
#     for i in ip:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     mf=max(d.values())
#     l=[]
#     for i in range(mf+1):
#         l.append([])
#     for i in d.items():
#         l[i[1]].append(i[0])
#     print(l)
#     for i in range(len(l)):
#         if i==len(l)-k:
#             print(l[i])
#     print(l[mf][len(l[mf])-k])
#     c=[]
#     for i in range(len(l)):
#         for j in l[i]:
#             c.extend([j]*i)
#     print(c)
#     print(c[len(c)-k])
# a=[2,13,4,2,9,9,5,7,7,13,3]
# bucketsort(a,3)

# sir
#find the Kth largest elements from the unsorted list 
# a=[3,6,13,8,5,4,7,13,8,2,7]
# k=3
# b=[0 for i in range(max(a)+1)]
# print(b)
# for i in a:
#   b[i]=1
# #   print(b)
# for i in range(len(b)-1,-1,-1):
#   if(b[i]==1):
#     k=k-1
#   if(k==0):
#     print(i)
#     break
  
# kth largest element                                     (higest ele is less than arr len)
# a=[3,6,13,8,5,6,4,7,13,8,2,7]
# k=3
# b=[0 for i in range(max(a)+1)]
# print(b)
# for i in a:
#     b[i]+=1
# print(b)
# for i in range(len(b)-1,-1,-1):
#     if(b[i]!=0):
#         k=k-b[i]
#     if(k<=0):
#         print(i)
#         break

# find the number which has highest of frequency , list has lot of duplicates
# a=[3,6,13,8,5,4,7,8,8,13,8,2,7]
# d={}
# for i in a:
#   if(i not in d):
#     d[i]=1
#   else:
#     d[i]+=1
# print(d)
# m=0
# for i,j in d.items():
#   if(j>m):
#     m=j
#     res=i
# print(res)      #printing the largest frequency

# kth largest frequency
# a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
# freq = {}
# k=3
# for i in a:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
# print(freq)
# m=max(freq.values())
# # print(m)
# b=[0 for i in range(m+1)]
# for i in freq:
#     b[freq[i]]=i
#     print(b)
# print(b[-k])

#  find the no , freq is > n/2
# a=[2,1,1,2,3,1,1]
# freq = {}
# for i in a:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
# print(freq)
# for k,v in freq.items():
#     if v>len(a)//2:
#         print(k)

# a=[2,1,1,2,3,1,1]
# for i in range(len(a)):
#     c=1
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             c+=1
#     if c>len(a)//2:
#         print(a[i])

# find a num whose freq is greater than n/2  (boyer moore algorithm)
# a=[2,1,1,2,3,1,1]
# a=[2,1,3,1,1,1,3]                              # res 2 1 3 1 ..
# c=0                                            # c=1,0,1,0,1,0,0...
# res=a[0]
# for i in range(len(a)-1):
#     if res==a[i]:
#         c+=1     
#     else:
#         c-=1
#         if c==0:
#             res=a[i] 
#             c=1    
# print(res)

# linear search unsorterd array print the index of last occurance of the array if not found return -1
# ip=[2,4,3,2,4,2,3,4,5]
# x=4
# def index(ip,x):
#     ind=-1
#     for i in range(len(ip)):
#         if ip[i]==x:
#             ind=i
#     return ind
# print(index(ip,x))

# a=[2,3,5,6,7,7,8,9,10,10,10,13,15]
# x=7
# l,r=0,len(a)-1
# while l<=r:
#     m=(l+r)//2
#     if a[m]==x:
#          print("Found")
#          break
#     elif x<a[m]:
#         r=m-1
#     else:
#         l=m+1

# return last occurance index of element found
a=[2,3,5,6,7,7,9,10,10,10,13,15]
x=9
l,r=0,len(a)-1
f=-1
while l<=r:
    m=(l+r)//2
    if a[m]==x:
        f=m
        l=m+1
    elif x>a[m]:
        l=m+1       
    elif x<a[m]:
        r=m-1
    if f==-1:
        f=l
print(f)

    
