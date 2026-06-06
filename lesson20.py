# # > 🚀 Vehicle nomli ota klass yarat:
# # - `brand`, `year` atributlari bo‘lsin.
# # > 🚗 Car nomli farzand klass yarat:
# # - `model` qo‘shimcha atributi bo‘lsin.
# # > Obyekt yaratib, ham parent, ham child atributlarini chop et.
# class Vehice:
#     def __init__(self, brand, year):
#         self.brand=brand
#         self.year=year
#     def get_brand(self):
#         return self.brand
#     def get_yaer(self):
#         return self.year
# class Car(Vehice):
#     def __init__(self, brand, year, model):
#         super().__init__(brand, year)
#         self.model=model
#     def get_model(self):
#         return self.model

# car1=Car("BMW", 2024, "F90")
# print(car1.brand,car1.model,car1.year)

# # > Person klassida name va contacts (ro‘yhat) atributlari bo‘lsin.
# # 1. Avval `copy.copy()` bilan nusxa oling, `contacts`ni o‘zgartiring va farqni ko‘ring.
# # 2.  So‘ng `copy.deepcopy()` qilib, yangisiga alohida contact qo‘shing.
# import copy
# class Person:
#     def __init__(self, name, contacts):
#         self.name=name
#         self.contacts=contacts
        
# person1 = Person("Alibek",["Shodiyor", "Aziz"])
# person2=copy.copy(person1)
# person2.contacts.append("Otabek")
# print(person1.contacts)
# print("-"*30)

# person3 = Person("Alibek",["Shodiyor", "Aziz"])
# person4=copy.deepcopy(person3)
# person4.contacts.append("Otabek")
# print(person3.contacts)
# print(person4.contacts)

# > BankAccount klassi yarat:
# > 
# - `balance` atributi
# - `deposit()` va `withdraw()` metodlari
# - `@classmethod` bilan jami hisoblar soni
# - `@staticmethod` bilan karta raqami validatsiyasi
# - `@property` bilan `balance`ni o‘qish va o‘zgartirish

class BankAccount:
    hisoblar=0
    def __init__(self, name, balance, card_number):
        self.name=name
        self._balance=balance
        self.card_number=card_number
        BankAccount.hisoblar+=1
    
    def deposit(self, narx):
        if narx > 0:
            self.balance += narx
            print(f"Kartangizga {narx} so'm qo'shildi!")
        else:
            print("Pul miqdori xato kiritildi!")
    def withdraw(self, narx):
        if narx<=0:
            print("Pul miqdori xato kiritildi!")
        elif self.balance < narx:
            print("Hisobingizda mablag' yetarli emas!")
        else:
            self.balance -= narx
            print(f"Kartangizdan {narx} so'm yechildi!")

    @classmethod
    def hisoblar_soni(cls):
        return cls.hisoblar
    
    @staticmethod
    def validatsiya(card_number):
        return len(card_number) == 16
    
    @property
    def show_balance(self):
        return f"Hisobingizda {self._balance} so'm bor"
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        self._balance=value

    

def hisob(mijoz):
    while True:
        print("1.Pul mablag'i qo'shish\n2.Pul mablag'i yechish\n3.Joriy balance\n0.Chiqish")
        menu=input("Tanlash: ")
        if menu == '1':
            n=int(input("Qancha qo'shmoqchisiz: "))
            mijoz.deposit(n)
        elif menu == '2':
            n=int(input("Qancha yechmoqchisiz: "))
            mijoz.withdraw(n)
        elif menu == '3':
            print(mijoz.show_balance)
        elif menu == '0':
            break
        else:
            print("Noto'g'ri amal!")
            continue


mijoz1=BankAccount("Alibek", 100000, "9860170101350974")
mijoz2=BankAccount("Asadbek", 120000, "8600013209341290")
mijozlar=[mijoz1,mijoz2]
print("Mijozlar soni: ", BankAccount.hisoblar_soni(), "<----- classmetod")
print("Validatsiya: ", mijoz1.validatsiya(mijoz1.card_number), "<------- staticmetod")
print("-"*30)
print("property")
print(f"{mijoz1.name} mablag'i: {mijoz1.balance}")
mijoz1.balance = 200000
print(f"{mijoz1.name} mablag'i: {mijoz1._balance}")
print("-"*30)

while True:
    print("Mijozlar".center(135))
    for mijoz in mijozlar:
        print(f"{mijoz.name}")   
    m=input("Kimning hisobiga kirmoqchisiz: ")
    if m == mijoz1.name:
        hisob(mijoz1)
    elif m == mijoz2.name:
        hisob(mijoz2)
    elif m == '0':
        break
    else:
        continue
