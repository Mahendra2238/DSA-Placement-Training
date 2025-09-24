# # take size and two dictionaries input and merge them and print if value in dict1 is same as dict2 value override it with dict2 value 
# def merge_dicts(dict1,dict2):
#     for key,value in dict2.items():
#         if key in dict1 and dict1[key]==value:
#             dict1[key]=value
#     dict1.update(dict2)
#     return dict1

# def get_input(prompt):
#     n=int(input(f"Enter no of items for {prompt}: "))
#     dictionary={}
#     for i in range(n):
#         key_value=input("Enter key and value: ").split()
#         key=key_value[0]
#         value=key_value[1]
#         dictionary[key]=value
#     return dictionary

# dict1=get_input("first dictionary")
# dict2=get_input("second dictionary")

# merged_dict=merge_dicts(dict1,dict2)
# for key,value in merged_dict.items():
#     print(f"{key} {value}")

#or 
# n = int(input())
# d = {}
# for i in range(n):
#     a,b = input().split()
#     d[a] = b
# for i in range(n):
#     a,b = input().split()
#     d[a] = b
# for i,j in d.items():
#     print(i,j)

# duplicates
# list1=list(map(int,input().split(" ")))
# dup=[]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if(list1[i] not in dup and list1[i]==list1[j]):
#             dup.append(list1[i])
# if(len(dup)>0):
#     for i in dup:
#         print(i,end=" ")
# else:
#     print("No duplicate")

# pattern with diagonals in box outline
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==j or j==n-i+1 or i==n or j==n: #j==2*i or i==2*j
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()

# missing number
# lst = list(map(int,input().split(' ')))
# count,flag = 0,0
# for i in lst:
#     if(count!=i):
#         break
#     count+=1
# print(count)

# # program that takes a list of integers and returns a dictionary where the keys are the unique elements of the list, and the values are the frequency of each element.
# list1=list(input().split(" "))  #1 2 2 3 3 3
# d={}
# for i in list1:
#     if(i not in d.keys()):
#         count=0
#         for j in list1:
#             if(i==j):
#                 count+=1
#         d[i]=count
# for i,j in d.items():
#     print(i,":",j)

# ar = [int(x) for x in input().split()]
# f = {}
# for i in ar:
#     if i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# for key, value in f.items():
#     print(f"{key}: {value}")

#  finds the binary equivalent of a number recursively.
# def bin(n):
#     if n>=1:
#         bin(n//2)
#     print(n%2,end="")
# n=(int(input()))
# bin(n)

# print(bin(5))
# print(bin(int(input()))[2:])

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j>n+1:
#             print("* ",end="")
#         elif i<=j:
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()

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

# n=int(input()) 
# def binary(n):
#     if n<0:
#         print(0)
#         return
#     if n>1:
#         binary(n//2) 
#     print(n%2,end="")

# binary(n)

# n=int(input())
# def fib(n):
#     return n if n<=1 else fib(n-1)+fib(n-2)
# # print(fib(n ))
# print("Invalid" if n<=0 else [fib(i) for i in range(n)])
# # print("Invalid" if n<=0 else *[fib(i) for i in range(n)]) (if can run multiple times until cond true but else only once)
# print(*[fib(i) for i in range(n)] if n>0 else "Invalid")

# n=int(input())
# def sod(n):
#     sum=0
#     while n>0:
#         d=n%10
#         sum+=d
#         n=n//10
#     return sum
# print(sod(n))

# n=int(input())
# def sod(n):
#     n=abs(n)
#     if n==0:
#         return 0
#     else:
#         return(n%10+sod(n//10))
# print(sod(n))
    
# print("hello "*5)
# print("2"+str(5))
# print(int("2")+5)
# print("2"+"5")
# print(2+"5") #TypeError

# a="one"
# b=int(a) #value error
# print("hello" #syntax error
# list=[1,2,3]
# print(list[5]) #index out of bound
# d={'a':1}
# print(d['b']) #key error

try:
    n=int(input())
    res=10/n
    print(f"Result: {res}")
except ZeroDivisionError:
    print("Zero Division Error")
finally:
    print("This message always prints")
