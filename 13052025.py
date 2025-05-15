# bitmanipulation , two pointer , sliding window, divide and conquer
'''
    0101   <<1
   01010   = 10
  0  1  0 1 0 0   = 20
 (32 16 8 4 2 1 = 16+4=20)
eg : 5<<1 => 5*2^1 = 10
     5<<2 => 5*2^2 = 20
x*2^y
where x is number to be shifted and y is no of shifts
'''
# even or odd using % operator
# n=int(input())
# if (n&1==1):
#     print("odd")
# else:
#     print("even")

'''
n%1==0 => even
n&1==1 => odd
'''
# n=int(input())
# r=n^1
# if r==n-1:
#     print("odd")
# elif r==n+1:
#     print("even")

'''
eg: 2^1=3,  3^1=2
    4^1=5,  5^1=4
    ...     ...
even => next number
odd  => prev number
'''
'''
2^1=3   3^2=1
4^3=0   5^4=1
'''

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s^=i
# print(s)

'''
O(1) T.C
XOR from 1 to n= 
n   <= if n mod 4= 0
1   <= if n mod 4= 1
n+1 <= if n mod 4= 2
0   <= if n mod 4= 3
'''
# n=int(input())
# if n%4==0:
#     print(n)
# elif n%4==1:
#     print(1)
# elif n%4==2:
#     print(n+1)
# elif n%4==3:
#     print(0)    

# in range
# def xor_upto(n):
#     if n%4==0:
#         return n
#     elif n%4==1:
#         return 1
#     elif n%4==2:
#         return n+1
#     elif n%4==3:
#         return 0 
# def xor_range(l,r):
#      return xor_upto(r)^xor_upto(l-1)
# m,n=map(int,input().split())
# print(xor_range(m,n))

'''
is the number power of 2   
'''
# O(1)
# import math
# def isPower(n):
#     p=math.log2(n)
#     if 2**int(p)==n:
#         return "yes"
#     else:
#         return "no"
# n=int(input())
# print(isPower(n))  

# # (or)
# O(logn)
# n=int(input())
# i=1
# while 1:
#     if 2**i==n:
#         print("Yes")
#         break
#     if n<2**i:
#         print("No")
#         break
#     i+=1

# # (or) O(1)
# n=int(input())
# if (n&(n-1)==0):
#     print("yes")
# else:
#     print("no")

# a = [2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
# # a=[1,2,3,2,3,4,5,6,7,8,9]
# l, r = 0, len(a)-1
# maxc = 0
# lst=[]
# while l < r:
#     c = 1
#     while l < r and a[l+1] == a[l] + 1:
#         c += 1
#         l += 1
#     maxc = max(maxc, c)
#     lst.append(c)
#     l += 1  
# print(lst)
# print(maxc)

s="aaabbaaaacccdde"
r=''
c=1
for i in range(len(s)-1):
    if s[i+1]==s[i]:
        c+=1
    else:
        r=r+s[i]+str(c)
        # r.append(s[i])
        # r.append(str(c))
        c=1
r=r+s[-1]+str(c)
print(r)
# print(''.join(l))
        
    
