# Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
# with open('pi.txt', 'r') as file:
#     pi = file.read()
#     pi = pi.rstrip() 
#     pi = pi.replace('\n','')
#     pi = float(pi)
#     print(pi)

# with open('file/matn.txt', 'r') as file:
#     matn=file.read()
#     print(matn)

# filenomi="file/matn.txt"
# with open(filenomi) as file:
#     matn=file.read()
#     print(matn)

# filenomi="file/matn.txt"
# with open(filenomi) as file:
#     for line in file:
#         print(line)

# filenomi="file/matn.txt"
# with open(filenomi) as file:
#     matn=file.readlines()
# print(matn)

# filenomi='file/talabalar.txt'
# with open(filenomi, 'w') as file:
#     file.write("Alibek Nosiraliyev")
    
# faylnomi = 'file/talabalar.txt'
# ism = 'Nosiraliyev Alibek'
# t_yil = 2006
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(t_yil)+'\n')

# faylnomi = 'file/talabalar.txt'
# ism="Baxtiyorov Shodiyor"
# t_yil="2007"
# with open(faylnomi, 'a') as file:
#     file.write(ism + '\n')
#     file.write(t_yil + '\n')

# Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π  soni nuqtadan so'ng million xona aniqlik bilan yozilgan). '
# Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. 
# Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
# yil= "9122006"
# with open('pi_million_digits.txt', 'r') as file:
#     pi=file.read()
#     pi = pi.rstrip()  
#     pi = pi.replace("\n", "")
#     pi = pi.replace(" ", "")
#     print(yil in pi)

# Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
# import pickle

# with open("pi.txt", "r") as file:
#     pi_text = file.read().replace("\n", "")

# pi = float(pi_text)

# with open("pi.pkl", "wb") as file:
#     pickle.dump(pi, file)

# print("Saqlandi:", pi)

# with open("pi.pkl", "rb") as file:
#     pi = pickle.load(file)

# print(pi)
# print(type(pi))

# Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing. '
# Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas). 
# o'tkazing va pickle yordamida yangi faylga saqlang.
# while True:
#     talaba = input("Talaba ismini kiriting (to'xtash uchun 0 ni kiriting): ")
#     if talaba=="0":
#         break
#     with open("talaba.txt", "a") as file:
#         file.write(talaba + "\n")
