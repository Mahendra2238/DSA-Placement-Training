# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def append(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#             self.next=None
#         else:
#             new_node=Node(data)
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=new_node
#             current=new_node
#     def ins_beg(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def ins_pos(self, data, pos):
#         current = self.head
#         while current and current.data != pos:
#             current = current.next
#         if current:
#             new_node = Node(data)
#             new_node.next = current.next
#             current.next = new_node
#         else:
#             print(f"Position '{pos}' not found in the list.")
#     def display(self):
#         if not self.head:
#             print("List is empty")
#             return 
#         else:
#             nodes=[]
#             current=self.head
#             while current:
#                 nodes.append(str(current.data))
#                 current=current.next
#             print("->".join(nodes))
# l=LinkedList()
# l.append(10)
# l.ins_beg('a')
# l.append(20)
# l.ins_pos("b",10)
# l.ins_pos(15,"b")
# l.display()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n or i==j or j==n-i+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

          
# def switch(lang):
#     if lang == "JavaScript":
#         return "You can become a web developer."
#     elif lang == "PHP":
#         return "You can become a backend developer."
#     elif lang == "Python":
#         return "You can become a Data Scientist"
#     elif lang == "Solidity":
#         return "You can become a Blockchain developer."
#     elif lang == "Java":
#         return "You can become a mobile app developer"

# print(switch("JavaScript"))   
# print(switch("PHP"))   
# print(switch("Java"))  

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def push(self,data):
#         new_node=Node(data)
#         if not self.top:
#             self.top=new_node
#         else:
#             new_node.next=self.top
#             self.top=new_node
#     def pop(self):
#         if not self.top:
#             print("Stack is empty")
#             return None
#         else:
#             popped_ele=self.top.data
#             self.top=self.top.next
#             return popped_ele
#     def display(self):
#         if not self.top:
#             print("stack is empty")
#             return None
#         else:
#             nodes=[]
#             current=self.top
#             while current:
#                 nodes.append(str(current.data))
#                 current=current.next
#             print("->".join(nodes))
# s=stack()
# s.push(10)
# # s.push('a')
# s.push(20)
# s.push(30)
# s.pop()
# s.display()

list=[1,3,5,6,7]
k=int(input())
k=k%10
print(list[k:]+list[:k])