# 1-masala. Bank Account (Encapsulation + Property)
class BankAccount:
    def __init__(self, hisob, balance):
        self.hisob=hisob
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Kartangizga {amount} so'm qo'shildi!")
        else:
            print("Mablag' noto'g'ri kiritildi!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Yechib olish uchun mablag' noto'g'ri kiritilgan!")
        elif self.__balance < amount:
            print("Hisobingizda mablag' yetarli emas!")
        else:
            self.__balance -= amount
            print(f"Kartangizga {amount} so'm yechildi!")

    @property
    def balance(self):
        return self.__balance

hisob1=BankAccount("Alibek", 100000)
hisob1.deposit(10000)
hisob1.withdraw(-10000)
print(f"Hisobingizda {hisob1.balance} so'm bor!")