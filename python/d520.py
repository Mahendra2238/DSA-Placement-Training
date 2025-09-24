# n=input()
# ls=[int(i) for i in n.split()]
# if len(n)<2:
#     print("Invalid")
# else:
#     ls.sort()
#     print(ls[-2])

# n=input()
# ls=[int(i) for i in n.split()]
# setp=set(ls)
# for i in setp:
#     print(i,end=" ")

# rotated list
# lst = list(map(int,input().split(" ")))
# k=int(input())
# for i in range(k):
#     temp = lst[-1]
#     for j in range(len(lst)-2,-1,-1):
#         lst[j+1] = lst[j]
#     lst[0] = temp
# for i in lst:
#     print(i,end=" ")

# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     # print("*"*((2*i)-1),end="")
#     print("*"*((2*i)-1))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i<=j):
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()

# rhombus
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i+j>n+1):
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i<=j):
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()

# hallow rhombus
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     if i==1:
#         print("*")
#     else:
#         print("*"+" "*((2*i)-3)+"*")  
# for i in range(n-1,0,-1):
#     print(" "*(n-i),end="")
#     if i==1:
#         print("*")
#     else:
#         print("*"+" "*((2*i)-3)+"*")

#String
# s="hello"
# b='python'
# c='''is'''
# d="""not a snake"""
# print(s+" "+b)#concatination
# print(s*3)# repetation
# print(s[0])
# print(len(s))
# print(len(d))

# slicing [start:stop:step] 
# s="hello world"
# print(s[::])
# print(s[:7:])
# print(s[0:10:3])
# print(s[5::])
# print(s[::5])
# print(s[:5:])
# print(s[::-1]) #reverse

# strip
# s=" Hello hero of the betalian "
# print(s.strip()) #it will remove spaces both sides
# print(s.lstrip())
# b="python"
# print(s+b)
# print(s.rstrip()+b)

#find
# print(s.find("llo"))
# print(s.find(" "))
# print(s.index("l"))
# for i in range(len(s)):
#     if s[i]=='o':
#         print(i)

# s="Hello world "
# print(s.upper())
# print(s.lower())
# print(s.replace("world","WORLD"))
# # isalpha
# # islower
# # isupper
# # isdigit
# print(s.startswith("hel"))
# # endswith
# # lstrip
# # rstrip
# # strip
# # split(" ")
# print("-".join(["a","b","c"]))
# # find("w")  first index of w 
# # rfind("w")  last  index of w 
# # index()
# # rindex()
# # len()
# b="sr University"
# # print(b.istitle())
# #isspace
# # print(b.isspace())
# print(b.swapcase())
# print(b.capitalize())
 
# s=input()
# n=int(input())
# h=s[0:n]
# v=s[n+1:len(s)]
# print(h+v)

# print(input()[::2])
# a=input()
# b=input()
# count1=0
# count2=0
# for i in a:
#     count1+=1
# for j in b:
#     count2+=1
# if count1>count2:
#     print(a)
# else:
#     print(b)
# print(count1,count2)

# ss=input()
# c=0
# for i in ss:
#     c+=1
# print(ss[0:2]+ss[c-2:c])

# Function   reusability, understandabiity
# built in , user-defined
# syntax  
# def function_name():
    # block of code
    # return values
# function_name() 

# s=input()
# def fun(s):
#     if len(s)>=2:
#         return s[:2]+s[-2:]
#     else:
#         return ""
# print(fun(s))

a=input()
b=input()
def ls(a,b):
    count1=0
    count2=0
    for i in a:
        count1+=1
    for j in b:
        count2+=1
    if count1>count2:
        return a
    else:
        return b
print(ls(a,b))