# max meetings in one room such that they do not overlap
# st=[0,3,8,1,5,7,9]
# et=[5,6,10,2,6,9,11]
# for i in range(len(st)-1):
#     min=i
#     for j in range(i+1,len(st)):
#         if et[j]<et[min]:
#             min=j
#     st[min],st[i]=st[i],st[min]
#     et[min],et[i]=et[i],et[min]
# print(st)
# print(et)
# m=1
# last_end=et[0]
# for i in range(1,len(st)):
#     if st[i]>last_end:
#         m+=1
#         last_end=et[i]
# print(m)

# s=[0,3,8,1,5,7,9]
# e=[5,6,10,2,6,9,11]
# b=list(zip(s,e))
# b.sort(key=lambda x: x[1])
# st=0
# c=0
# for i in b:
#     if(i[0]>=st):
#         c+=1
#         st=i[1]+1
# print(c)

# reverse the given strings without changing the position of vowels
# s = list("hippopotomus")
# vowels = list("aeiou")
# consonants = [c for c in s if c not in vowels][::-1]
# result = []
# cindex = 0
# for ch in s:
#     if ch in vowels:
#         result.append(ch)
#     else:
#         result.append(consonants[cindex])
#         cindex += 1
# print("".join(result))  # Output: simtopopapuh


# s = list("hippopotomus")
# vowels = set("aeiou")
# l, r = 0, len(s) - 1
# while l < r:
#     if s[l] in vowels:
#         l += 1
#     elif s[r] in vowels:
#         r -= 1
#     else:
#         s[l], s[r] = s[r], s[l]
#         l += 1
#         r -= 1
# print("".join(s))  # Output: simtopopapuh

# max discount ,  add continuous k elements subarray and return max 
# ip=[2,1,4,4,2,3,1,1,4,2,4,2,6,7,3]
# k=5
# tsum=0
# ind=[0,k-1]
# for i in range(len(ip)-k+1):
#     sum=0
#     for j in range(i,i+k):
#         sum+=ip[j]
#     if sum>tsum:
#         tsum=sum
#         ind=[i,i+k-1]
# print(ind)
# print(tsum)

# in subarray u cant skip it should be contiginous but subsequence can be skipped(all subarr are subsequences also)
# a = [2, 1, 4, 4, 2, 3, 1, 1, 4, 2, 4, 2, 6, 7, 3]
# k = 5
# s = sum(a[:k])
# max_sum = s
# start_index = 0
# for r in range(k, len(a)):
#     s = s - a[r - k] + a[r]
#     if s > max_sum:
#         max_sum = s
#         start_index = r - k + 1
# print(f"Max sum window: {a[start_index:start_index + k]}")
# print(f"Indices: [{start_index}, {start_index + k - 1}]")

# sum also should be <= k
# a=[2,1,4,4,2,3,1,1,4,2,4,2,6,7,3]
# l=0
# k=6
# m=0
# sum=0
# for r in range(len(a)):
#     sum+=a[r]
#     if sum<=k:
#         m=max(m,r-l+1) #find length between l and r
#     else:
#         sum-=a[l]
#         l+=1
# print(m)

# length of longest palindromic substring
# s="ababba"
# m=0
# for i in range(len(s)):
#     l=r=i
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         m=max(m,r-l+1)
#         l=l-1
#         r=r+1
#     l=i
#     r=i+1
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         m=max(m,r-l+1)
#         l=l-1
#         r=r+1
# print(m)

# longest palindrome
# s="ababba"
# m=0
# st_ind=0
# for i in range(len(s)):
#     l=r=i
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         if (r-l+1)>m:
#             m=r-l+1
#             st_ind=l
#         l=l-1
#         r=r+1
#     l=i
#     r=i+1
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         if (r-l+1)>m:
#             m=r-l+1
#             st_ind=l
#         l=l-1
#         r=r+1
# print(s[st_ind:st_ind+m])

# # count of all possible substrings
# s="ababba"
# m=0
# st_ind=0
# c=0
# for i in range(len(s)): #even and odd
#     l=r=i
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         c+=1
#         if (r-l+1)>m:
#             m=r-l+1
#             st_ind=l
#         l=l-1
#         r=r+1
#     l=i
#     r=i+1
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         c+=1
#         if (r-l+1)>m:           
#             m=r-l+1
#             st_ind=l
#         l=l-1
#         r=r+1
# print(m)
# print(s[st_ind:st_ind+m])
# print(c)

# length of longest sub string without repeating char
s = "abcdaecdb"
l = 0
m = 0
d = {}
for r in range(len(s)):
    if s[r] in d and d[s[r]] >= l:
        l = d[s[r]] + 1  # Move left pointer just past the last occurrence
    d[s[r]] = r
    m = max(m, r - l + 1)
print(d)
print(m)
