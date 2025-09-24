# fibonacci series
# a=0
# b=1
# n=int(input("Enter number: "))
# #print(a,b,end=" ")
# if (n==1):
#     print(a)
# elif (n==2):
#     print(b)
# else:
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#     print(c,end=" ")

# using recursion
# def fib(n):
#     if(n==1):
#         return 0
#     if(n==2):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input("Enter number: "))
# print(fib(n))

# area = 500.2300
# print(f"area: {area:.2f}")

#factorial or not using for
# n=int(input("Enter n: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     if(fact!=n):
#         if(i>=n):
#             print("No")
#         else:
#             continue
#     else:
#         print("Yes")
#         break
#or
# n = int(input("Enter a number: "))
# fact = 1 
# for i in range(1, n+1):
#     fact *= i
# if fact == n:
#     print("Yes")
# elif fact > n:
#     print("No")

#using while
# n=int(input("Enter n value: "))
# i=1
# factorial=1
# while factorial<n:
#     i+=1
#     factorial*=i
# if(factorial==n):
#     print("yes")
# else:
#     print("no")

#exceed 100 vending machine
# sum=0
# while sum<100:
#     n=int(input("Enter number: "))
#     sum+=n
# print("Target Reached")

# sum=0
# for i in range(0,5):   
#     n=int(input("Enter number: "))
#     sum+=n
# if sum>=100:
#     print("Target Reached")

# Overtime workers
# count=0
# n=int(input("Enter number of workers: "))
# for i in range(1,n+1):
#     whoe=int(input(f"Enter working hrs of employee {i}: "))
#     if(whoe>8):
#         count+=1
# print("Overtime Workers: ",count)

# n=int(input("Enter number: "))
# sum=0
# # n=abs(n)
# # while n!=0:
# while n>0:
#     d=n%10
#     sum+=d
#     n=n//10
# print(sum) 

#for loop
# n=int(input("Enter number: "))
# sum=0
# l=len(str(n))
# for i in range (l):
#     sum+=n%10
#     n//=10
# print(f"Sum of digits: {sum}")

# until single digit sum
# number = int(input())
# while number >= 10:
#     sum_of_digits = 0
#     while number > 0:
#         sum_of_digits += number % 10
#         number //= 10
#     number = sum_of_digits
#print(f"Single digit: {number}")

#word count
#print(len(input("Enter text: ").split()))

# text=input("Enter text: ")
# count=len(text.split())
# print(count)

# line = input("enter text: ")
# count =1
# for i in range(0,len(line)):
#   if(line[i]==' '):
#     count+=1
# print(count)

# sentence = input(" ")
# words = sentence.split()
# word_count = len(words)
# print(f"Word count: {word_count}")

#armstron of n digits
# n=int(input("Enter number: "))
# sum=0
# temp=n
# p=len(str(n))
# while temp>0:
#     r=temp%10
#     sum+=r**p
#     temp=temp//10 
# if(sum==n):
#     print(f"{sum} is a armstrong number")
# else: 
#     print(f"{n} is not a armstrong number")

# n=int(input("Enter number: "))
# s=5
# for i in range(1,(2*n)-1):
#         if i%2!=0:
#             s+=11*i
#             print(s)

# n=int(input())
# t=5
# d=11
# for i in range(n):
#     print(t,end=" ")
#     t+=d
#     d+=22

# for i in range(1,15,2):
#     print(i)
# n=int(input("Enter number: "))
# s=5
# for i in range(1,(2*n)-1,2):
#         s+=11*i
#         print(s)

#patterns
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# #p
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i+j>=n+1):
#             print("* ",end="")
#         else:
#             print("  ",end="") #extra space
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i<=j):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i>=j):
#             print("* ",end="")
#         else:
#             print(" ",end="") #extra space
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i+j<=n+1):
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()

#rhombus
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     for j in range(i+1)  :
#         print("* ",end="")  
#     print()  
     
# for i in reversed(range(n+1)):
#     for j in range(n-i):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     for j in range(i+1)  :
#         print("* ",end="")  
#     print()

# n=int(input("Enter n: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# n=int(input("Enter n: "))
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==2:
#             print(f"{k}*",end=" ")
#             k+=1
#         else:
#             print(f"{k}-",end=" ")
#             k+=1
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n-i+1):
#         print(n-j-i+1 ,end=" ") 
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(n,n-i,-1):
#         print(j ,end=" ") 
#     print()
# for i in range(5):
#     print(i)