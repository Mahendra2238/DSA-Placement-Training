# import sys
# print(sys.getrecursionlimit())

# what does empty return returns? None
# n=0
# def p(n):
#     if n<1:
#         return
#     else:
#         return n
# print(p(n))

# To write empty functions in Python, we use pass statement. pass is a special statement that does nothing. It only works as a dummy statement.
# def fun():
#     pass  # Function logic to be added later
# # Calling the empty function
# fun()  # This does nothing for now

# OOPS-  class
# c=5
# class sru:
#     a=10
#     def dis(self): # self is used in instance method
#          b=15
#          print(b)
# obj=sru()
# obj.dis()
# print(obj.a)
# print(c)

# class Mobile:
#     def __init__(self,brand,ram): # ,camera,battery):
#         self.brand=brand
#         self.ram=ram
#         # self.camera=camera
#         # self.battery=battery
#     def display(self):
#         print("Brand: ",self.brand,"\n","ram: ",self.ram)
# # o=Mobile("Dell","8GB","64mp","1000mah")
# brand,ram=input().split(" ")
# o=Mobile(brand,ram)
# o.display()

# class animal:
#     def __init__(self,name):
#         self.name=name
#         print("parent constructor")
#     def eat(self):
#         print("It eats")
# class dog(animal):
#     def __init__(self):
#         print("child constructor")
#     # super().eat()
#     def eat(self,name):
#         print(f"It eats {name}")
# o=dog()
# # o.eat()
# o.eat("bones")

# Multilevel
# class Parent:
#     def display(self):
#         print("Parent Class")
# class Child(Parent):
#     def display1(self):
#         print("Child Class")
        
# class GChild(Child):
#     def display2(self):
#         print("Grand Child Class")
# obj=GChild()
# obj.display()
# obj.display1()
# obj.display2()

# class vehicle:
#     def __init__(self,brand,max_speed):
#         self.brand=brand
#         self.max_speed=max_speed
#     def display_vehicle(self):
#         print("Vehicle Info:\nBrand:",self.brand,"\nMax Speed: ",self.max_speed,"km/h")
# class car(vehicle):
#     def __init__(self,brand,max_speed,type):
#         super().__init__(brand,max_speed)
#         self.type=type
#     def display_car(self):
#         print("Car Info:\nType: ",self.type)
# class sportsCar(car):
#     def __init__(self,brand,max_speed,type,high_performance):
#         super().__init__(brand,max_speed,type)
#         self.high_performance=high_performance
#     def display_sportsCar(self):
#         print("Sports Car Info:")
#         per="Yes" if self.high_performance else "No"
#         print(f"High-performance: {per}")
#         # if self.high_performance=="True".casefold():
#         #     print("High-performance: Yes")
#         # elif self.high_performance=="False".casefold():
#         #     print("High-Performance: No")
#         # else:
#         #     print("Invalid input")
# brand=input()
# max_speed=int(input())
# type=input()
# high_performance=input().lower()=="true"
# v=sportsCar(brand,max_speed,type,high_performance)
# v.display_vehicle()
# v.display_car()
# v.display_sportsCar()

# class player:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def pd(self):
#         print(f"players_Details:\nName:{self.name}\nage:{self.age}")
# class batsman(player):
#     def __init__(self,name,age,runs,avg):
#         super().__init__(name,age)
#         self.runs=runs
#         self.avg=avg
#     def bmd(self):
#         print(f"Batsman Details:\nRuns: {self.runs}\nAverage: {self.avg}")
# class captain(batsman):
#     def __init__(self,name,age,runs,avg,capt):
#         super().__init__(name,age,runs,avg)
#         self.capt=capt
#     def cptd(self):
#         print(f"Captain info:\nIs Captain:{'Yes' if self.capt else 'No'}")
# name=input()
# age=int(input())
# runs=int(input())
# avg=float(input())
# capt=input().lower()=="true"
# p=captain(name,age,runs,avg,capt)
# p.pd()
# p.bmd()
# p.cptd()

# class Vehicle:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed        
#     def display_vehicle(self):
#         print("Vehicle Info:")
#         print(f"Brand : {self.brand} Max Speed : {self.speed} kmph")

# class carinfo:
#     def __init__(self,type):
#         self.type=type 
#     def display_car(self):
#         print(f"Car Info : \nType :{self.type}")

# class sports(Vehicle,carinfo):
#     def __init__(self,brand,speed,type,perf):
#         Vehicle.__init__(self,brand,speed)
#         carinfo.__init__(self,type)
#         self.perf=perf 
#     def display_perf(self):
#         perf_status="Yes" if self.perf else "No"
#         print(f"Sports Car Info:\nHigh-Performance: {perf_status}")    
# brand=input()       
# speed=int(input())
# type=input()
# perf=input().lower()=="true"
# obj=sports(brand,speed,type,perf)
# obj.display_vehicle()
# obj.display_car()
# obj.display_perf()

# Hierarchical 
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def display_vehicle(self):
        print("Vehicle Info:")
        print(f"Brand: {self.brand}, Max Speed: {self.speed} kmph")
class CarInfo(Vehicle):
    def __init__(self, brand, speed, car_type):
        super().__init__(brand, speed)
        self.car_type = car_type
    def display_car(self):
        print("Car Info:")
        print(f"Type: {self.car_type}")
class Sports(Vehicle):
    def __init__(self, brand, speed, perf):
        super().__init__(brand, speed)
        self.perf = perf
    def display_perf(self):
        perf_status = "Yes" if self.perf else "No"
        print("Sports Car Info:")
        print(f"High-Performance: {perf_status}")
brand = input()
speed = int(input())
car_type = input()
perf = input().lower() == "true"
car_obj = CarInfo(brand, speed, car_type)
sports_obj = Sports(brand, speed, perf)
car_obj.display_vehicle()
car_obj.display_car()
sports_obj.display_vehicle()
sports_obj.display_perf()