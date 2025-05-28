# eg. floor value of 3,4 is 3 and 8.9 is 8
# eg. ceil value of 4.2 is 5 and -3.7 is -3

# square root of number
# import math
# num = 166
# sqrt = num ** 0.5
# print(sqrt)  # Output: 4.0

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
# print(f"{ans:.{p}f}")
# # print(round(ans,2))
# if they ask for ceil give l if floor give r

#given rotated array return index of target
# def search(nums,target):
#     l=0
#     h=len(nums)-1
#     while l<=h:
#         m=(l+h)//2
#         if nums[m]==target:
#             return m
#         if  nums[l]<=nums[m]:
#             if target>=nums[l] and target<=nums[m]:
#                 h=m-1
#             else:
#                 l=m+1
#         else:
#             if target>=nums[m] and target<=nums[h]:
#                 l=m+1
#             else:
#                 h=m-1                 
#     return -1
# a=[10,20,30,40,50,60,70,0,5,6,7,8,9]
# t=0
# print(search(a,t))

# return index of min element in rotated arr
# def search(a):
#     l=0
#     r=len(a)-1
#     while l<r:
#         m=(l+r)//2
#         if  a[r]<a[m]:
#             l=m+1
#         else:
#             r=m               
#     return [r,a[r]]
# a=[10,20,30,40,50,60,70,0,5,6,7,8,9]
# print(search(a))

# peak element
# def search(a):
#     l=0
#     r=len(a)-1
#     while l<=r:
#         m=(l+r)//2
#         if m==0 or a[m]>a[m-1] and m==len(a) or a[m]>a[m+1]:
#             print(a[m])
#             break
#         if a[m+1]>a[m]:
#             l=m+1
#         else:
#             r=m-1
# a=[2,3,4,6,3,2,1,5,3,10,1,4,2]
# search(a)

# Koko Eating Bananas
# import math
# def koko(b,h,k):
#     # possible=False
#     s=0
#     for i in b:
#         s=s+math.ceil(i/k)
#         if s>h:
#             return False
#     return True  #s<=h
#     # if s<=h:
#     #     possible=True
#     # return [s,possible] 
# piles=[3,5,7,11]
# hours=8
# speed=4
# print(koko(piles,hours,speed))

# o(n*m)
# import math
# def koko(b,h,k=1):
#     s=0
#     s = sum(math.ceil(i / k) for i in b)
#     if s<=h:
#         return k
#     return koko(b,h,k+1)
# piles=[3,5,7,11]
# hours=8
# print(koko(piles,hours))

# import math
# def koko(b,h):
#     k=1
#     while(1):
#         s=0
#         for i in b:
#             s=s+math.ceil(i/k)
#             if s>h:
#                 k+=1
#                 break
#         else:
#             return k
# piles=[3,5,7,11]
# hours=8
# print(koko(piles,hours))

# def koko(piles,h):
#     l,r=0,max(piles)
#     while l<r:
#         k=(l+r)//2
#         hs=sum((p+k-1)//k for p in piles)
#         if hs>h:
#             l=k+1
#         else:
#             r=k
#     return l
# piles=[3,5,7,11]
# hours=8
# print(koko(piles,hours))

# # sir o(nlogm)
# import math
# def possibleornot(piles, k, h):
#     s = 0
#     for i in piles:
#         s += math.ceil(i / k)
#         if s > h:
#             break
#     if s<=h:
#         return True
#     else:
#         return False
# def minEatingSpeed(piles, h):
#     l = 1
#     r = max(piles)
#     res = r
#     while l <= r:
#         m = (l + r) // 2
#         if possibleornot(piles, m, h):
#             res = m
#             r = m - 1
#         else:
#             l = m + 1
#     return res
# piles = [3, 5, 7, 11]
# hours = 8
# print(minEatingSpeed(piles, hours))

# Aggressive Cows
# def agressivecowsPossible(s,k,m):
#     s.sort()
#     prev=s[0]
#     k-=1
#     for i in range(1,len(s)):
#         if s[i]-prev>=m:
#             prev=s[i]
#             k-=1
#         if k==0:
#             return True
#     return False
# stalls=[2, 12, 11, 3, 26, 7]
# cows = 3
# mindist=5
# print(agressivecowsPossible(stalls,cows,mindist))

# s = [2, 12, 11, 3, 26, 7]
# k = 3
# m = 5
# s.sort()
# while True:
#     prev = s[0]
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] - prev >= m:
#             prev = s[i]
#             count += 1
#     if count >= k:
#         m += 1
#     else:
#         break
# print(m - 1)

# def can_place(s, k, m):
#     count = 1
#     prev = s[0]
#     for i in range(1, len(s)):
#         if s[i] - prev >= m:
#             count += 1
#             prev = s[i]
#         if count == k:
#             return True
#     return False
# def aggressive_cows(s, k, m=1):
#     s.sort()
#     if can_place(s, k, m):
#         return aggressive_cows(s, k, m + 1)
#     return m - 1
# stalls = [2, 12, 11, 3, 26, 7]
# cows = 3
# print(aggressive_cows(stalls, cows))

# with binary
# def aggressiveCows(s, k):
#     def isPos(s,n,k,m):
#         laststall=s[0]
#         c=1
#         for i in range(1,n):
#             if s[i]-laststall>=m:
#                 laststall=s[i]
#                 c+=1     
#             if c==k:
#                 return True
#         return False
#     s.sort()
#     n=len(s)
#     ans=0
#     start=1
#     end=s[-1]-s[0] #max val -min val
#     while start<=end:
#         mid=(start+end)//2
#         if isPos(s,n,k,mid):
#             ans=mid
#             start=mid+1
#         else:
#             end=mid-1
#     return ans
# stalls = [2, 12, 11, 3, 26, 7]
# cows = 3
# print(aggressiveCows(stalls, cows))