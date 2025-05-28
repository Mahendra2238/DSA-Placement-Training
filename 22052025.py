# # start and reach out of arr . fuel will be deducted by 1 when we move to next or can be exchanged with the next element accordingly
# a = [2, 1, 2, 0, 3, 8]
# s = a[0]
# for i in range(1, len(a)):
#     s -= 1  
#     if s < 0:
#         print("Not possible")
#         break
#     if a[i] > s:
#         s = a[i]  
# else:
#     print("Possible")

# # Jump game
# class Solution:
#     def canJump(self, a: List[int]) -> bool:
#         reach=0
#         for i in range(len(a)):
#             if i>reach:
#                 return False
#             reach=max(reach,i+a[i])
#             if reach>=len(a)-1:
#                 return True
#         return False

# Lemonade Change  -a lemon juice cost 5₹ to do business possible or not c
# c = [5, 5, 10, 5, 20]
# c5, c10 = 0, 0
# for i in c:
#     if i == 5:
#         c5 += 1
#     elif i == 10:
#         if c5 > 0:
#             c5 -= 1
#             c10 += 1
#         else:
#             print("False")
#             break
#     else:  # i == 20
#         if c10 > 0 and c5 > 0:
#             c10 -= 1
#             c5 -= 1
#         elif c5 >= 3:
#             c5 -= 3
#         else:
#             print("False")
#             break
# else:
#     print("True")

# min avg waiting time
# ip=[5,3,7,1,6,2]
# ip.sort()
# s=0
# ts=0
# for i in ip:
#     s+=i
#     ts+=s
# avg=ts//len(ip)
# print(avg)

# people and schemes bundle are given find max startups possible, scheme money can be given equal or more than required.  nlogn
# p=[1,6,2,3,4,5]
# s=[4,2,3,1,1,2]
# p.sort()  # 1 2 3 4 5 6
# s.sort()  # 1 1 2 2 3 4
# # 1 2 3 4
# i=j=0
# while i<len(p) and j<len(s):
#     if p[i]<=s[j]:
#         i+=1
#     j+=1
# print(i)

# jump game 2: min no of jumps
# a=[2,3,1,1,4]
# l=0
# r=0
# f=0
# jumps=0
# while (r<len(a)-1):
#     maxj=0
#     for i in range(l,r+1):
#         if (i+a[i])>maxj:
#             maxj=i+a[i]
#         if maxj>=len(a)-1:
#             f=1
#             break
#     l=r+1
#     r=maxj
#     jumps+=1
#     if f==1:
#         break
# print(jumps)

# exam
# square root with precision using binary search
# n=38
# l=1
# h=n
# ans=0
# p=3
# while l<h:
#     m=(l+h)/2
#     msqr=m*m
#     if msqr==n:
#         ans=m
#         break
#     elif msqr<n:
#         l=m+1
#     else:
#         h=m-1
#     ans=h
# # print(f"{ans:.{p}f}")
# print(round(ans,p))



