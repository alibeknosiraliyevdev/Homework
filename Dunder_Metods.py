# 1. CustomClass nomli klass yaratib, uning ustiga yuqorida keltirilgan dunder methodsni qo'shing 
# (masalan, __add__, __eq__, __str__, __getitem__, va h.k.).
# 2. Keyin bu klassni sinab ko'ring, obyektlar yaratib, ular bilan amaliyotlar bajaring.
class CustomClass:
    def __init__(self, qiymat):
        self.qiymat = qiymat

    def __str__(self):
        return f"CustomClass({self.qiymat})"

    def __repr__(self):
        return f"CustomClass({self.qiymat})"

    def __add__(self, other):
        return CustomClass(self.qiymat + other.qiymat)

    def __eq__(self, other):
        return self.qiymat == other.qiymat

    def __lt__(self, other):
        return self.qiymat < other.qiymat

    def __len__(self):
        return len(str(self.qiymat))
    
    def __getitem__(self, index):
        return str(self.qiymat)[index]

    def __contains__(self, item):
        return str(item) in str(self.qiymat)

obj1 = CustomClass(34)
obj2 = CustomClass(23)
obj3 = CustomClass(45)

print(obj1)
print(obj1 + obj2)
print(obj1 == obj3)
print(obj1 < obj2)
print(len(obj1))
print(obj1[1])
print(3 in obj1)



