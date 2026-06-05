# # 1. Car class yozish
# class Car:
#     def __init__(self , model, rang, turi, yoqilgi_turi):
#         self.model=model
#         self.rang=rang
#         self.turi=turi
#         self.yoqilgi_turi=yoqilgi_turi

#     def info(self):
#         print(self.model,self.rang,self.turi,self.yoqilgi_turi)

# car1=Car("BMW", "Qora", "Mexanik", "Benzin")
# car1.info()

# # 2. Teacher class yozish
# class Teacher:
#     def __init__(self, name, age, fan_nomi, lavozimi):
#         self.name=name
#         self.age=age
#         self.fan_nomi=fan_nomi
#         self.lavozimi=lavozimi
    
#     def info(self):
#         print(self.name,self.age ,self.fan_nomi, self.lavozimi)

# teacher1=Teacher("Xojiakbar", 34, "Elektronika va Sxemalari", "Dotsent")
# teacher1.info()        

# # 3. Animal → Cat inheritance qilish
# class Animal:
#     def __init__(self, name, zoti, ranggi):
#         self.name=name
#         self.zoti=zoti
#         self.ranggi=ranggi

# class Cat(Animal):
#     def __init__(self, name, zoti, ranggi, ovozi):
#         super().__init__(name, zoti, ranggi)
#         self.ovozi=ovozi

#     def info(self):
#         print(f"Mushuk: {self.name}, {self.zoti}, {self.ranggi}, {self.ovozi}")
    
# cat1=Cat("Mosh" , "Shvetsariya mushugi", "Malla", "Meow")
# cat1.info()

# # 4. Getter/Setter qo‘shish
# class Car:
#     def __init__(self , model, rang, turi, yoqilgi_turi):
#         self.model=model
#         self.rang=rang
#         self.turi=turi
#         self.yoqilgi_turi=yoqilgi_turi

#     def get_model(self):
#         return self.model
    
#     def set_turi(self, new_turi):
#         self.turi=new_turi   
#         return self.turi

# car1=Car("BMW", "Qora", "Mexanik", "Benzin")
# print(car1.get_model())
# print(car1.set_turi("Avtomat"))

# # 5. Polymorphism misoli yozish
# class Animal:
#     def sound(self):
#         print("Hayvon ovozi")

# class Dog(Animal):
#     def sound(self):
#         print("Vov-vov")

# class Cat(Animal):
#     def sound(self):
#         print("Miyov-miyov")

# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.sound()

##################################################################################################################################
# # - `Vehicle` nomli **asosiy (parent) klass** yarat.
# # - Undan `Car` va `Bike` nomli **ikki farzand klass** meros olsin.
# # - Har bir klassda umumiy va o‘ziga xos metodlar bo‘lsin.
# # - Klasslardan obyektlar yaratib, metodlarini chaqir.
# class Vehicle:
#     def __init__(self, turi):
#         self.turi=turi

#     def start(self):
#         print(f"{self.turi} yurishni boshladi")
#     def stop(self):
#         print(f"{self.turi} yurishni to'xtatdi")
        
# class Car(Vehicle):
#     def __init__(self, turi, model):
#         super().__init__(turi)
#         self.model=model
    
#     def eshik_ochilishi(self):
#         print(f"{self.model} eshigi ochildi")

# class Bike(Vehicle):
#     def __init__(self, turi, bike_turi):
#         super().__init__(turi)
#         self.bike_turi=bike_turi

#     def qongiroq(self):
#         print(f"{self.bike_turi} velosipedining qo'ng'irog'i chalindi")

# car1=Car("Avtomodil", "Lacetti Gentra")
# bike1=Bike("Velosiped", "Phantom")
# print("------------------------------------------")
# car1.start()
# car1.eshik_ochilishi()
# car1.stop()
# print("------------------------------------------")
# bike1.start()
# bike1.qongiroq()
# bike1.stop()

##################################################################################################################################
# # 1. **Student** nomli asosiy (parent) klassini yarat. Ushbu klassda talabalar uchun umumiy ma'lumotlar bo'lsin: ism, yosh, va baho.
# class Student:
#     def __init__(self, ism, yosh, baho):
#         self.ism=ism
#         self.yosh=yosh
#         self.baho=baho
#     def info(self):
#         print(f"Ism: {self.ism}\nYosh: {self.yosh}\nBaho: {self.baho}")

# std1=Student("Ali", 20, 90)
# std1.info()
        
# # 2. `age` va `grade` atributlarini **private** qilib belgilash. Faqat getter va setter metodlari 
# # orqali bu atributlarga kirish mumkin bo'lsin.
# class Student:
#     def __init__(self, surname, name, age, grade):
#         self.surname=surname
#         self.name=name
#         self.__age=age
#         self.__grade=grade

#     def info(self):
#         print(self.surname,self.name)

#     def get_age(self):
#         return self.__age
#     def get_grade(self):
#         return self.__grade
#     def set_age(self, age):
#         self.__age=age
#         return self.__age
#     def set_grade(self, grade):
#         self.__grade=grade
#         return self.__grade

# std1=Student("Nosiraliyev","Alibek", 20, "2-kurs")
# std1.info()
# print("Age:",std1.get_age())
# print("Grade:",std1.get_grade())
# print("------------------------------------------")
# print("Age:",std1.set_age("21"))
# print("Grade:",std1.set_grade("3-kurs"))

# # 3. Talaba ismini o'zgartirish uchun **public** metod yaratilsin (boshqa atributlar faqat getter 
# # va setter metodlari orqali o'zgartirilishi kerak).
# class Talaba:
#     def __init__(self, ism, yosh, grade):
#         self.__ism=ism
#         self.__yosh=yosh
#         self.__grade=grade

#     def new_ism(self, yangi_ism):
#         self.__ism=yangi_ism
#     def get_ism(self):
#         return self.__ism
#     def get_yosh(self):
#         return self.__yosh
#     def get_grade(self):
#         return self.__grade
#     def set_age(self, yosh):
#         self.__yosh=yosh
#         return self.__yosh
#     def set_grade(self, grade):
#         self.__grade=grade
#         return self.__grade

# ta1=Talaba("Alibek", 20, "2-kurs")
# ta1.new_ism("Asadbek")
# print("Ism:", ta1.get_ism())
# print("Yosh:", ta1.get_yosh())
# print("Kurs:", ta1.get_grade())

# # 4. Shuningdek, **age** atributi faqat ijobiy qiymatlarni qabul qilishi kerak va **grade** atributi 
# # faqat 0 va 100 orasidagi qiymatlarni qabul qilishi kerak.
# class Student:
#     def __init__(self, name, age, grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_grade(self):
#         return self.grade
    
#     def set_age(self, new_age):
#         self.age=new_age
#         return self.age
#     def set_grade(self, new_grade):
#         self.grade=new_grade
#         return self.grade
    
# std1=Student("Ali", 19, 2)
# print("Ism:",std1.get_name())
# print("Yosh:",std1.get_age())
# print("Grade:",std1.get_grade())
# print("-"*20)
# n_age=int(input("Yangi yosh: "))
# n_grade=int(input("Yangi grade: "))
# print("-"*20)
# if n_age >= 0:
#     std1.set_age(n_age)
#     if n_grade >0 and n_grade<100:
#         std1.set_grade(n_grade)
#         print("Ism:",std1.get_name())
#         print("Yangi yosh:",std1.get_age())
#         print("Yangi grade:",std1.get_grade())
#     else:
#         print("Grade 0 va 100 orasida emas!")
# else:
#     print("Manfiy yosh bo'lmaydi!")


# 5. Talaba haqida ma'lumotlarni chiqaruvchi metodlar va bu metodlarni sinovdan o'tkazish uchun bir nechta obyektlar yaratilsin.
class Talaba:
    def __init__(self, ism, yosh, grade):
        self.ism=ism
        self.yosh=yosh
        self.grade=grade

    def get_ism(self):
        return self.ism
    def get_yosh(self):
        return self.yosh
    def get_grade(self):
        return self.grade
    
    def set_ism(self, yangi_ism):
        self.ism=yangi_ism
        return self.ism
    def set_age(self, yosh):
        self.yosh=yosh
        return self.yosh
    def set_grade(self, grade):
        self.grade=grade
        return self.grade
    
    def kurs(self):
        if self.yosh >=20:
            print(f"Ism:{self.ism}\nYosh:{self.yosh}\nKurs:{self.grade}")
            print("-"*20)
        else:
            print("Bunday yoshdagi talabalar mavjud emas!")
            print("-"*20)

ta1=Talaba("Alibek", 20, "2-kurs")
ta2=Talaba("Jamshidbek", 19, "1-kurs")
ta3=Talaba("Amirbek", 21, "3-kurs")
ta4=Talaba("Shodiyor", 19, "2-kurs")

talabalar=[ta1,ta2,ta3,ta4]

for talaba in talabalar:
    print("Ism:", talaba.get_ism())
    print("Yosh:", talaba.get_yosh())
    print("Kurs:", talaba.get_grade())
    print("-"*20)

print("Saralangan talabalar\n")
for talaba in talabalar:
    talaba.kurs()
    