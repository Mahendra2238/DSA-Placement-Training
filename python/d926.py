# def max_profit(prices):
#     maxp=0
#     for i in range(1,len(prices)):
#         for j in range(i+1,len(prices)):
#             # p=prices[j]-prices[i]
#             # if p>maxp:
#             #     maxp=p
#             maxp=max(maxp,prices[j]-prices[i])
#     return maxp
# prices=[7,4,2,1]
# print(max_profit(prices))

# Data Structures
# Linked List
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
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=new_node
#     def display(self):
#         if not self.head:
#             print("List is Empty")
#         else:
#             nodes=[]
#             current=self.head
#             while current:
#                 nodes.append(str(current.data))
#                 current=current.next
#             print("->".join(nodes))
# l=LinkedList()
# # l.append(10)
# # l.append('a')
# # l.append(10.3)
# # l.append("hi")
# # l.display()
# op="yes"
# while op=="yes":
#     i=input("Enter value: ")
#     op=input("Enter 'yes' to continue else enter any key to exit: ")
#     l.append(i)
# l.display()
            
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
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next 
#             current.next=new_node 
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def insert_at_position(self,data,pos):
#         if not self.head:
#             self.head=new_node 
#         else:
#             current = self.head
#             while current.next and current.next.data != pos:
#                 current = current.next
#             current=current.next
#             if current.next:
#                 new_node=Node(data)
#                 new_node.next=current.next
#                 current.next = new_node
#             else:
#                 print("Node not found.")
#     def delete(self, data):
#         if not self.head:
#             print("List is empty.")
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         current = self.head
#         while current.next and current.next.data != data:
#             current = current.next
#         if current.next:
#             current.next = current.next.next
#         else:
#             print("Node not found.")
#     def display(self):
#         if not self.head:
#             print("The list is empty")
#         nodes=[]
#         current=self.head 
#         while current:
#             nodes.append(str(current.data))
#             current=current.next 
#         print("-> ".join(nodes))
# def user_interface():
#     ll = LinkedList()
#     while True:
#         print("\nChoose an option:")
#         print("1. Append an element")
#         print("2. Insert at the beginning")
#         print("3. Insert at the position")
#         print("4. Delete an element")
#         print("5. Display the list")
#         print("6. Exit")
#         choice = int(input("Enter your choice: "))

#         if choice == "1":
#             data = int(input("Enter the element to append: "))
#             ll.append(data)
#         elif choice == "2":
#             data = int(input("Enter the element to insert at the beginning: "))
#             ll.insert_at_beginning(data)
#         elif choice == "3":
#             data = int(input("Enter the element to insert at the position: "))
#             pos=int(input("Enter the position value: "))
#             ll.insert_at_position(data,pos)
#         elif choice == "4":
#             data = int(input("Enter the element to delete: "))
#             ll.delete(data)
#         elif choice == "5":
#             print("Current list:")
#             ll.display()
#         elif choice == "6":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# user_interface()

# Stack using linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.top
#         self.top=new_node
#     def pop(self):
#         if not self.top:
#             print("Stack is Empty")
#             return
#         else:
#             popped_data=self.top.data
#             self.top=self.top.next
#             # return popped_data
#             print("popped element: ",popped_data)
#     def display(self):
#         if not self.top:
#             print("Stack is Empty")
#             return
#         else:
#             nodes=[]
#             current=self.top
#             while current:
#                 nodes.append(current.data)
#                 current=current.next
#             print("".join(str(nodes)))
#     def peek(self):
#         if not self.top:
#             print("Stack is Empty")
#             return None
#         return self.top.data
#     def is_empty(self):
#         return self.top is None
# s=stack()
# s.push(30)
# s.push(20)
# s.push(100)
# s.pop()
# print("Peek Element: ",s.peek())
# print("stack is Empty? ",s.is_empty())
# s.display()

# Queue using linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None
#     def enqueue(self,data):
#         if not self.rear:
#             new_node=Node(data)
#             self.front=self.rear =new_node
#         else:
#             new_node=Node(data)
#             self.rear.next=new_node
#             self.rear=new_node
#     def dequeue(self):
#         if not self.front:
#             print("Queue is empty")
#             return None
#         else:
#             dequeued_data=self.front.data
#             self.front=self.front.next
#             if not self.front:
#                 self.front=None
#                 return dequeued_data
#     def peek(self):
#         if not self.front:
#             print("Queue is empty")
#             return None
#         return self.front.data
#     def is_empty(self):
#         return self.front is None
#     def display(self):
#         if not self.front:
#             print("Queue is empty")
#             return
#         else:
#             nodes=[]
#             current=self.front
#             while current:
#                 nodes.append(str(current.data))
#                 current=current.next
#             print("->".join(nodes))
# q=Queue()
# q.enqueue(10)
# q.enqueue(15)
# q.enqueue(20)
# q.dequeue()
# print("peek element: ",q.peek())
# print("Queue is Empty?",q.is_empty())
# q.display()


