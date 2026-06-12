# # 1-masala. Bank Account (Encapsulation + Property)
# class BankAccount:
#     def __init__(self, hisob, balance):
#         self.hisob=hisob
#         self.__balance=balance

#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Kartangizga {amount} so'm qo'shildi!")
#         else:
#             print("Mablag' noto'g'ri kiritildi!")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Yechib olish uchun mablag' noto'g'ri kiritilgan!")
#         elif self.__balance < amount:
#             print("Hisobingizda mablag' yetarli emas!")
#         else:
#             self.__balance -= amount
#             print(f"Kartangizga {amount} so'm yechildi!")

#     @property
#     def balance(self):
#         return self.__balance

# hisob1=BankAccount("Alibek", 100000)
# hisob1.deposit(10000)
# hisob1.withdraw(-10000)
# print(f"Hisobingizda {hisob1.balance} so'm bor!")

# # 2-masala. Employee va Manager (Inheritance)
# class Employee:
#     def __init__(self, name, salary):
#         self.name=name
#         self.salary=salary

#     def show_info(self):
#         print(f"Ism: {self.name}\nMaosh: {self.salary}$")

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department=department

#     def show_info(self):
#         super().show_info()
#         print(f"Bo'lim: {self.department}")

# manager1=Manager("Alibek", 3000, "Backend")

# manager1.show_info()

# # 3-masala. Shape (Polymorphism)
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius=radius

#     def area(self):
#         return f"Aylana yuzasi: {3.14 * self.radius*self.radius}"
    
# class Rectangle(Shape):
#     def __init__(self, kenglik, uzunlik):
#         self.kenglik=kenglik
#         self.uzunlik=uzunlik

#     def area(self):
#         return f"To'rtburchak yuzasi: {self.kenglik * self.uzunlik}"
    
# shapes=[Circle(5), Rectangle(3, 4)]

# for shape in shapes:
#     print(shape.area())

# # 4-masala. Temperature (Property)
# class Temperatura:
#     def __init__(self, celsius):
#         self._celsius=celsius

#     @property
#     def celsius(self):
#         if self._celsius < -273.15:
#             print("False")
#         else:
#             print("True")

# cel1=Temperatura(273)
# cel2=Temperatura(-300)

# cel1.celsius
# cel2.celsius

# # 5-masala. Student (Class Method)
# class Student:
#     hisoblar=0
#     def __init__(self , name):
#         self.name= name
#         Student.hisoblar+=1

#     @classmethod
#     def student_count(cls):
#         return cls.hisoblar

# std1=Student("Ali")

# print(Student.student_count())

# # 6-masala. Calculator (Static Method)
# class Calculator:

#     @staticmethod
#     def add(a , b):
#         return a + b
#     @staticmethod
#     def subtract(a, b):
#         return a-b
#     @staticmethod
#     def multiply(a, b):
#         return a*b
#     @staticmethod
#     def divide(a, b):
#         return a/b
    
# math=Calculator()

# print(Calculator.add(3,4))
# print(Calculator.subtract(3,4))
# print(Calculator.multiply(3,4))
# print(Calculator.divide(3,4))

# # 7-masala. Product (Property Setter)
# class Product:
#     def __init__(self, name, price):
#         self.name=name
#         self.price=price

#     @property
#     def narx(self):
#         return self.price
#     @narx.setter
#     def narx(self, value):
#         self.price=value
#         if value > 0:
#             return self.price
#         else:
#             print("False")

# mahsulot1=Product("Non", 3000)

# print(mahsulot1.narx)
# mahsulot1.narx = 0
# mahsulot1.narx = -3000

# # 8-masala. Animal Hierarchy (Polymorphism)
# class Animal:
#     def speak(self):
#         print("Hayvon ovozi")
    
# class Dog(Animal):
#     def speak(self):
#         print('Wow ladi!')

# class Cat(Animal):
#     def speak(self):
#         print('Meow ladi!') 
    
# class Cow(Animal):

#     def speak(self):
#         print('Moo ladi!')
    
# animals=[Dog(), Cat(), Cow()]
# for animal in animals:
#     animal.speak()

# # 9-masala. User Factory (Class Method)
# class UserFactory:

#     @classmethod
#     def from_email(cls, email:str):
#         return email.split("@")[0]
    
# print(UserFactory.from_email("ali@gujgvhkk"))

# # 10-masala. Rectangle (Dunder Method)
# class Rectangle:
#     def __init__(self, kenglik, uzunlik):
#         self.kenglik=kenglik
#         self.uzunlik=uzunlik
    
#     def __str__(self):
#         return f"Rectangle({self.kenglik},{self.uzunlik})"
    
# rect=Rectangle(10,20)
# print(rect)

# # 11-masala. Online Shop Product
# class Product:
#     count=0
#     def __init__(self, name, price):
#         self.name=name
#         self.__price=price
#         Product.count += 1

#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self, narx):
#         if narx > 0:
#             self.__price=narx
#         else:
#             print("Narx manfiy bulmaydi!")

#     @classmethod
#     def from_discounted_price(cls, name, discounted_price, discounted_foiz):
#         haqiqiy_price=discounted_price/(1-discounted_foiz/100)
#         return cls(name, haqiqiy_price)
    
#     def info(self):
#         print(f"Nomi: {self.name}")
#         print(f"Narxi: {self.price}")

# p1 = Product.from_discounted_price("Telefon",900,10)
# p2 = Product.from_discounted_price("Noutbook",1000,20)

# p1.info()
# p2.info()
# print("Mahsulotlar soni:", Product.count)

# # 12-masala. Vector (Dunder Methods)
# class Vector:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
    
#     def __str__(self):
#         return  f"Vector({self.x}, {self.y})"
    
# obj1=Vector(2,3)
# obj2=Vector(4,5)

# print(obj1+obj2)
# print(obj1-obj2)

# # 13-masala. Library Management System
# from abc import ABC, abstractmethod
# class LibraryItem(ABC):
#     @abstractmethod
#     def borrow(self):
#         pass

# class Book(LibraryItem):
#     def borrow(self):
#         return 'Kitob 30 kun uchun olindi'
    
# class Magazine(LibraryItem):
#     def borrow(self):
#         return 'Jurnal 15 kun uchun olindi'
    
# class DVD(LibraryItem):
#     def borrow(self):
#         return 'DVD 7 kun uchun olindi'
    
# objects=[Book(), Magazine(), DVD()]
# for object in objects:
#     print(object.borrow())

# # 14-masala. Smart Bank Account
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance=balance

#     def __add__(self, other):
#         return self.__balance + other.__balance
        
# acc1=BankAccount(100)
# acc2=BankAccount(200)

# print(acc1+acc2)

