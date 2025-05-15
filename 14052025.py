# # function
# def qwer(x,y=200):
#     print("hi",x,y)
#     return 20
# b=qwer(10)
# print(b)

# def qwer(x=100,y): # will give error cannot place positional argument after default arg as there is no use of default if we give like that
#     print("hi",x,y)
#     return 20
# b=qwer(10)
# print(b)

# def qwer(x,y,z,u):
#     print("hi",x,y,z,u)
#     return 20
# b=qwer(y=10,x=20,z=30,40) # will be error as you are giving keyword arg and taking rights from system to assign independently positional.
# print(b)

# def qwer():
#     print("hello")
#     asd()
# def zxc():
#     print("hey")
#     qwer()
# def asd():
#     print("namaste")
#     print("1")
# qwer()
# print("9")
# zxc()

# def qwer():
#     print("hi")
#     qwer()           # until stack overflow  (while loop goes for infinite we use break statement to stop loop)
# qwer()

# Recursion

# import sys
# sys.setrecursionlimit(3000)  # limit is 1000 by default i.e, hi will be printed 999 times and gives error at 1000 time. But we can set recursion limit if we want
# def qwer(x):
#     print("hi",x)
#     qwer(x+1)
# qwer(1)

# we use return stmt to stop recursion
# def qwer(x):
#     print("hi",x)
#     return
#     qwer(x+1)
# qwer(1)

# def qwer(x):
#     if(x==6):
#         return
#     print("hi",x)
#     qwer(x+1)
# qwer(1)
# print("hello")

# def qwer(x):         # recursion will store every stack call it can route/trace back in the same path unlike for loop   (first half entry rotation, second half exit rotation)
#     if(x==6):
#         return
#     print("hi",x)
#     qwer(x+1)
#     print("hi",x)
# qwer(1)
# print("hello")
# return stmt=> send you back to the 

# def qwer(x):
#     if(x==4):
#         return 200
#     print("hi",x)
#     qwer(x+1)
#     print("hi",x)
# b=qwer(1)
# print(b) # 200 is not printing because it is returned to only most recent call and remaining with none and atlast with none
 
# def qwer(x):
#     if(x==4):
#         return 200
#     print("hi",x)
#     t=qwer(x+1)
#     print("hi",x)
#     return t       # now it will print 200 as we storing in t and returning 20o to calls  
# b=qwer(1)
# print(b)

# def qwer(x):
#     if(x==4):
#         return 200
#     print("hi",x)
#     t=qwer(x+1)
#     print("hi",x)
#     return t+x     
# b=qwer(1)
# print(b)

# def qwer(x):
#     if(x==4):
#         return 20
#     return x+qwer(x+1)     #1+2+3+20=26
# b=qwer(1)
# print(b)

# def qwer(x):
#     if(x==1):
#         return 1
#     return x*qwer(x-1)     #5*4*3*2*1=120
# b=qwer(5)
# print(b)

# def qwer(x):
#     if(x==1):
#         return 1
#     if (x==2):
#         return 1
#     return qwer(x-1)+qwer(x-2)+x
# b=qwer(5)
# print(b)

# def qwer(x):
#     if(x==1):
#         return 1
#     if (x==2):
#         return 1
#     return qwer(x-1)+qwer(x-2)
# b=qwer(8)
# print(b)

# do not use recursion where it is unnecessary
n = int(input("Enter the value of n: "))
if n <= 0:
    print("Invalid input! n must be at least 1.")
elif n == 1:
    print(0)
else:
    a = [0] * n
    a[0], a[1] = 0, 1
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    print(a[n-1])


# def even_sum(x,i):
#     if i==len(x):
#         return 0
#     if x[i]%2==0:
#         return x[i]+even_sum(x,i+1)
#     else:
#         return even_sum(x,i+1)
# a=[2,5,6,7,2,1,4,3,6]
# print(even_sum(a,0))

# reverse a number using recursion
# def rev(n,re):
#     if n==0:
#         return re
#     return rev((n//10),re*10+(n%10))
# n=int(input())
# print(rev(n,0))

# def isPrime(n,k=2):
#     if n<2:
#         return False
#     if k>(n//2):
#         return True
#     if n%k==0:
#         return False
#     return isPrime(n,k+1)
# def count_prime(lst,i,c):
#     if i==len(lst):
#         return c
#     else:
#         if isPrime(lst[i]):
#             return count_prime(lst,i+1,c+1)
#         else:
#             return count_prime(lst,i+1,c)
# lst=[13,17,21,23,22,7,29,31]
# print(count_prime(lst,0,0))

# def check(n):
#     if n==1:
#         return 0
#     if n<1:
#         return float('inf')
#     stepby3=check(n-3)
#     stepby5=check(n-5)
#     return min(stepby3,stepby5)+1
# n=int(input())
# res=check(n)
# if res==float('inf'):
#     print("Not possible")
# else:
#     print("Min steps to reach 1: ",res)

# def qwer(x,n,m):
#     if(x==1):
#         return True
#     if x<1:
#         return False
#     return qwer(x-n,n,m) or qwer(x-m,n,m)
# x,n,m=20,3,5
# print(qwer(x,n,m))

# def qwer(x,n,m):
#     if(x==1):
#         return 0
#     if x<1:
#         return float('inf')
#     return min(qwer(x-n,n,m), qwer(x-m,n,m))+1
# x,n,m=20,3,5
# print(qwer(x,n,m))

# bfs is less time consuming than dfs. but when shortest path or longest path type dfs is better

#bfs
