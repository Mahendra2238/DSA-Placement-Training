# n=127
# for i in range(1,n+1):
#     print(chr(i),end=" ")
# print()

#break & continue
# for i in range(6):
#     if i==3:
#         print()
#         print(f"Execution is paused at value of {i}")
#         # break
#         continue
#     print(i,end=' ')

#lists
# ordered changable/mutable duplicates [] 
# # List:
# ->if we want to represent group of elements in a single entity
# then we will go for lists.
# ->the insertion order is preserved and it will allows duplicate values
# ->it will allows heterogenous(different) objects
# a=[1,"hello",4.555,{5,3}] print(3,0,-1)
# a[1]=5
# ->list is dynamic we can increase and decrease the size of the list

# based on our requirement

# ->In list the elements should be placed within the square braces
# and separated by commas

# ->we can access the list elements by using index positions

# ->the index position will starts with 0 and ends with size-1

# ->list will support negative indexing also
# the negative index starts with -1 and goes on.

# *->List objects are mutable(changable) we can change the list objects
# a=[1,2,3]
# print(a)
# print(type(a))

# n=int(input())
# a=[]
# for i in range (1,n+1):
#     v=int(input())
#     a.append(v)
# print()
# print(max(a))
# or
# n=int(input())
# list=[]
# for i in range (1,n+1):
#     list.append(int(input()))
# max=list[0]
# for i in list:
#     if i>max:
#         max=i
# print(max)
# list=[]
# n=int(input())
# sum=0
# if n<=15:
#     for i in range(n):
#         list.append(int(input()))
#         sum+=list[i]
#     print("sum: "+str(sum))
#     list.sort()
#     print(list[0],list[-1])
#     print(sum-list[0]-list[1])
# print(len(list))

# def sum_array(arr):
#     #your code here
#     sum=0
#     if len(arr)<2:
#         return 0
#     else:
#         for i in range (0,len(arr)):
#             sum+=arr[i]
#         arr.sort()
#         sum=sum-arr[0]-arr[-1]
#         return sum
# arr=[]
# n=int(input())
# for i in range(n):
#     arr.append(int(input()))
# print(sum_array(arr))
# list=[1,2]
# print(len(list))

# n=int(input())
# list=[]
# if n<=15:
#     for i in range(n):
#         list.append(int(input()))
#     count=n
#     for i in range(n):
#         for j in range(n):
#             if(list[i]==list[j]):
#                 count-=1
#             break
# print("distinct ele: "+str(count))

# n = int(input())
# list_ = []
# if n <= 15:
#     for i in range(n):
#         list_.append(int(input()))
#     # Create a set to store unique elements
#     unique_elements = set(list_)
#     # The count of unique elements is the size of the set
#     count = len(unique_elements)
# print(count)
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# l1=[1,2,3,2]
# l2=l1.copy()
# print(l2.count(2))
# print(l2)
# a=input()
# print(tuple(reversed(a)))
# list.append("one")
# # list.clear()
# l2=list.copy()
# print(l2.count(2))
# print(l2)
# list=[1,2,2,3] # 0 1 2 3 n//2 + (n//2)-1
# list2=[6,7,8]# 0 1 2 n//2
# list2.extend(list)
# list.reverse()
# print(list)
# print(list2)

#tuples
# a=("one","two","three")
# print(a)
# b=(1,2,3)
# print(a+b)
# for i in a:
#     print(i)

#zip and unzip
# n=3
# a=[]  # [(1, 3, 8), (2, 4, 9)]
# for i in range(n):
#     tup=tuple(map(int,input().split()))
#     a.append(tup)
# print(list(zip(*a)))

# a=10
# b=20
# c=30
# t=a,b,c # packing
# print(t)
# a,b,c=t #unpacking
# print(a,b,c)

#set
# Python has a set of built-in methods that you can use on sets.

# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
# set={"one","two","three","two",1}
# set2={1,2,3}
# set.update(set2)
# print(set & set2)
# print(set)
# print(set | set2)
# # set.add("four")
# # set.remove("two")
# # for i in sorted(set):  #to not print in random order use sorted
# #     print(i)
# # set.add("four")
# # print(set)
# # print(type(set))

# #dictionary
# # Python has a set of built-in methods that you can use on dictionaries.

# # Method	Description
# # clear()	Removes all the elements from the dictionary
# # copy()	Returns a copy of the dictionary
# # fromkeys()	Returns a dictionary with the specified keys and value
# # get()	Returns the value of the specified key
# # items()	Returns a list containing a tuple for each key value pair
# # keys()	Returns a list containing the dictionary's keys
# # pop()	Removes the element with the specified key
# # popitem()	Removes the last inserted key-value pair
# # setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# # update()	Updates the dictionary with the specified key-value pairs
# # values()	Returns a list of all the values in the dictionary
# dict=   {"Roll No":123,
#         "Name":"Hemanth",
#         "Year":"3rd year"}
# print(dict["Name"]) 
# # x=dict.keys()
# dict["branch"]="cse"
# print(dict)
# dict["clg"]="SRU"
# print(dict)

# dict.pop("Year")
# print(dict.values())
# print(dict.keys)
# print(list("abc"))
# x+y for x in [1,2] 
# l=[1,2,3,]
# print(l.clear())