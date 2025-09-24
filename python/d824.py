# diamond
# n=int(input())
# for i in range(n):
#     print(" "*(n-i-1),"* "*(i+1),end="")
#     print()
# for j in range(n):
#     print(" "*(j+1),"* "*(n-j-1),end="")
#     print()

# 1 121 12321 diamond
# rows = int(input())
# for i in range(1,2*rows):
#     k = 0
#     if i <= rows:
#         limit = i # upper half
#     else:
#         limit = 2*rows-i  # Lower half
#     for space in range(1, rows-limit+1):
#         print(" ", end="")
#     for j in range(1,2*rows):
#         if j <= limit:
#             k += 1
#         else:
#             k -= 1
#             if k <= 0:
#                 break
#         print(k, end="")
#     print()
# or
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print(j+1,end="")
#     for j in range(i)  :
#         print(i-j,end="")
#     print()
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
        
#         print(j+1,end="")
#     for j in range(i)  :
#         print(i-j,end="")
#     print()
# or
# n=int(input())
# def pyramid(n):
#     for i in range(1,n+1): #upper pyramid
#         left=" ".join(map(str,range(1,i+1)))
#         right=" ".join(map(str,range(i-1,0,-1)))
#         space=" "*(2*(n-i))
#         print(space+left+" "+right)
#     for i in range(n-1,0,-1): #lower pyramid
#         left=" ".join(map(str,range(1,i+1)))
#         right=" ".join(map(str,range(i-1,0,-1)))
#         space=" "*(2*(n-i))
#         print(space+left+" "+right)
# pyramid(n)

#Butterfly upper pyramid
# n=int(input())
# def pyramid(n):
#     for i in range(1,n+1): #upper pyramid
#         right="* "*i
#         space="  "*(n-i)*2
#         left="* "*i 
#         print(right+space+left)
# pyramid(n)

# Butterfly
# n=int(input())
# def pyramid(n):
#     for i in range(1,n+1): #upper pyramid
#         right="* "*i
#         space="  "*(n-i)*2
#         left="* "*i 
#         print(right+space+left)
#     for i in range(n,0,-1): #lower pyramid
#         right="* "*i
#         space="  "*(n-i)*2
#         left="* "*i 
#         print(right+space+left)
# pyramid(n)

# n=6
# for i in range (n):
#     for j in range(i+1):
#         print(j+1,end="")
#     for j in range(2*(n-i-1)):
#         print(" ",end="")
#     for j in range (i+1):
#         print(i-j+1,end="")
#     print()
# for i in range (n-2,-1,-1):
#     for j in range(i+1):
#         print(j+1,end="")
#     for j in range(2*(n-i-1)):
#         print(" ",end="")
#     for j in range (i+1):
#         print(i-j+1,end="")
#     print()

# Anagrams
# str=input().split()
# d={}
# for word in str:
#     sw=''.join(sorted(word))
#     if sw in d:
#         d[sw].append(word)
#     else:
#         d[sw]=[word] 
# for group in d.values():
#     print(*group)
# # for key,value in d.items():
# #     print(f"{key} {value}")

# Method overloading
# class Addition:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c=0):
#         return a+b+c
#     def add(self,a,b,c=0,d=0):
#         return a+b+c+d
# ob=Addition()
# print(ob.add(12,2))
# print(ob.add(12,2,6))
# print(ob.add(12,2,6,10))

# class husband:
#     def house(self):
#         print("Husband House")
#     def land(self):
#         print("Husband land")
#     def money(self):
#         print("Husband money")
# class wife:
#     def house(self):
#         print("wife House")
#     def land(self):
#         print("wife land")
#     def money(self):
#         print("wife money")
# obj=wife()
# obj.house()
# obj.money()

# class husband:
#     def house(self):
#         print("Husband House")
#     def land(self):
#         print("Husband land")
#     def money(self):
#         print("Husband money")
# class wife(husband):
#     def house(self):
#         super().house()
#         print("wife House")
#     def land(self):
#         super().land()
#         print("wife land")
#     def money(self):
#         super().money()
#         print("wife money")       
# obj=wife()
# obj.house()
# obj.money()

#override
# class Animal:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#     def display(self):
#         print(f"Type: {self.type}\nName: {self.name}")
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
# type = input("Enter type (Dog/Cat): ")
# name = input("Enter name: ")
# animal = Dog(name,type) if type.lower() == "dog" else Cat(name,type)
# print("Animal Info:")
# animal.display()
# print("Sound:", end=' ')
# animal.sound()

# Encapsulation-   Encapsulation is one of the four principles used in Object Oriented Paradigm. It is used to bind and hide data to the class. Data hiding is also referred as Scoping and the accessibility of a method or a field of a class can be changed by the developer. 
# single underscore _ -protected,  double underscore __ -private
# class Student:
#     def __init__(self,name,roll_no,fees):
#         self.name=name
#         self.roll_no=roll_no
#         self.__fees=fees
#         self.__fees_paid=0
    
#     def pay_fees(self,amount):
#         if 0<amount<=self.__fees-self.__fees_paid:
#             self.__fees_paid+=amount
#             print(f"Paid:{amount}")
    
#     def display(self):
#         print(f"Name : {self.name},Roll No : {self.roll_no}")
#         print(f"Total : {self.__fees},Paid : {self.__fees_paid},Remaining : {self.__fees-self.__fees_paid}")
        
# student=Student("DHEERAJ",32,130000)
# student.display()
# student.pay_fees(20000)
# student.display()
# student.pay_fees(46000)
# student.display()

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.borrowed_books = {}
        self.total_fine = 0
    def borrow_book(self, book_name):
        if len(self.borrowed_books) < 3:
            if book_name not in self.borrowed_books:
                self.borrowed_books[book_name] = 0  # Day count starts from 0
                print(f'{self.name} (Roll No: {self.roll_no}) borrowed "{book_name}".')
            else:
                print(f'{self.name} (Roll No: {self.roll_no}) already borrowed "{book_name}".')
        else:
            print(f"{self.name} (Roll No: {self.roll_no}) cannot borrow more than 3 books.")
    def return_book(self, book_name, days_borrowed):
        if book_name in self.borrowed_books:
            del self.borrowed_books[book_name]
            if days_borrowed > 7:
                fine = (days_borrowed - 7) * 5
                self.total_fine += fine
                print(f'{self.name} (Roll No: {self.roll_no}) returned "{book_name}" after {days_borrowed} days.')
                print(f'Fine for "{book_name}": ₹{fine}.')
            else:
                print(f'{self.name} (Roll No: {self.roll_no}) returned "{book_name}" on time.')
        else:
            print(f'{self.name} (Roll No: {self.roll_no}) did not borrow "{book_name}".')
    def view_account(self):
        borrowed_books_list = ', '.join(self.borrowed_books.keys())
        borrowed_books_list = borrowed_books_list if borrowed_books_list else "None"
        print(f"Account Details:")
        print(f"Borrowed Books: {borrowed_books_list}")
        print(f"Total Fine: ₹{self.total_fine}")

def main():
    alice = Student("Alice", 101)
    alice.borrow_book("Pride and Prejudice")
    alice.borrow_book("Harry Potter")
    alice.return_book("Harry Potter", 10)
    alice.view_account()
    print("\n")
    bob = Student("Bob", 202)
    bob.borrow_book("The Great Gatsby")
    bob.borrow_book("1984")
    bob.view_account()
main()


# abstract 
# from abc import ABC, abstractmethod
# class Student(ABC):
#     def __init__(self, name, roll_no, fees):
#         self.name = name
#         self.roll_no = roll_no
#         self._fees = fees
#         self._fees_paid = 0
#     @abstractmethod
#     def pay_fees(self, amount):
#         pass
#     @abstractmethod
#     def display(self):
#         pass
# class Student1(Student):
#     def pay_fees(self, amount):
#         if 0 < amount <= self._fees - self._fees_paid:
#             self._fees_paid += amount
#             print(f"Paid: {amount}")
#     def display(self):
#         print(f"Name : {self.name}, Roll No : {self.roll_no}")
#         print(f"Total : {self._fees}, Paid : {self._fees_paid}, Remaining : {self._fees - self._fees_paid}")
# student = Student1("DHEERAJ", 32, 130000)
# student.display()
# student.pay_fees(20000)
# student.display()
# student.pay_fees(46000)
# student.display()
