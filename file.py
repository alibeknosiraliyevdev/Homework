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

####################################################📄 TXT (File I/O) — 10 EASY ####################################################

# 1. Faylga yozish
# # Foydalanuvchi kiritgan ismni `names.txt` ga yoz.
# ism = input("Ismingizni kiriting: ")
# with open('names.txt', 'w') as file:
#     file.write(ism)
#     print("Faylga ism kiritildi")

# # ### 2. Faylni o‘qish
# # `names.txt` faylidagi barcha ma’lumotni ekranga chiqar.
# with open('names.txt', 'r') as file:
#     names=file.read()
#     print(names)

# # ### 3. Bitta qator yozish
# # Faylga “Hello World” matnini yoz.
# with open('hello.txt', 'w') as file:
#     file.write('Hello World')
# print("Matn yozildi")

# # ### 4. Fayl mavjudligini tekshirish
# # Fayl bor yoki yo‘qligini tekshir.
# with open('hello.txt', 'r') as file:
#     if file.read():
#         print('Fayl mavjud')
#     else:
#         print('Fayl mavjud emas')

# ### 5. Bo‘sh fayl yaratish
# `empty.txt` fayl yarat.
# with open('empty.txt', 'w') as file:
#     pass
# print('Fayl yaratildi')

# ### 6. 3 ta satr yozish
# Foydalanuvchidan 3 ta so‘z olib faylga yoz.
# with open('words.txt', 'w') as file:
#     n=int(input('Nechta so\'z kiritmoqchisiz: '))
#     for i in range(n):
#         soz=input(f'{i+1}-so\'zni kiriting: ')
#         file.write(soz + '\n')
#     print('Faylga so\'zlar yozildi')

# # ### 7. Faylni to‘liq o‘qish
# # `words.txt` ni to‘liq o‘qib chiq.
# with open('words.txt' , 'r') as file:
#     matn=file.read()
# print(matn)

# # ### 8. Qatorlar soni
# # Fayldagi qatorlar sonini chiqar.
# with open('words.txt', 'r') as file:
#     qatorlar = file.readlines()
# print("Qatorlar soni:", len(qatorlar))

# # ### 9. Faylga qo‘shish (append)
# # Yangi matnni fayl oxiriga qo‘sh.
# name=input("ism kiriting: ")
# with open('names.txt', 'a') as file:
#     file.write('\n'+name)
# print("Faylga malumot qo'shildi")

# # ### 10. Faylni tozalash
# # Fayl ichidagi barcha ma’lumotni o‘chir.
# with open('names.txt', 'w'):
#     pass
# print('Malumotlar o\'chirildi!')

####################################################📄 TXT — 10 MEDIUM ####################################################

# # ### 1. So‘zlar soni
# # Fayldagi barcha so‘zlar sonini hisobla.
########## split()- matndan so'zni kesib olish
# with open('words.txt', 'r') as file:
#     matn=file.read()
# sozlar=matn.split()
# print('Matn so\'zlar soni:', len(sozlar))

# # ### 2. Eng uzun so‘z
# # Fayldagi eng uzun so‘zni top.
# with open('words.txt', 'r') as file:
#     matn=file.read()
# sozlar=matn.split()
# eng_uzun = max(sozlar, key=len)
# print('Matn eng uzun so\'z:', eng_uzun)

# # ### 3. Qidiruv
# # Fayldan berilgan so‘zni top va nechta marta kelganini chiqar.
##### lower()- matnni kichik harflarga o'tqizish
# with open('matn.txt', 'r') as file:
#     matn=file.read().lower()
# soz=input("Qidiruv: ").lower()
# soni=matn.split().count(soz)
# print(f"{soz} so'zi matnda {soni} marta qatnashgan")

# # ### 4. ERROR hisoblash
# # log.txt ichida “ERROR” nechta ekanini san.
# with open('log.txt', 'w') as file:
#     pass
# with open('log.txt', 'r') as file:
#     matn=file.read()
# soz="ERROR"
# soni=matn.split().count(soz)
# print(f"{soz} so'zi {soni} marta qatnashgan")

# ### 5. Faylni teskari o‘qish
# Fayldagi qatorlarni teskari tartibda chiqar.
######## readline()- matnni qatorlar bilan o'qish
######## reversed()- bu ketma-ketlik elementlariga teskari tartibda kiradigan iteratorni qaytaradigan o'rnatilgan funksiya
######## strip()- boshidagi va oxiridagi boʻshliqlarni yoki koʻrsatilgan belgilarni olib tashlash uchun ishlatiladi. 
# with open('matn.txt', 'r') as file:
#     matn=file.readlines()
# for qator in reversed(matn):
#     print(qator.strip())

# # ### 6. Palindrom so‘zlar
# # Fayldagi palindrom so‘zlarni top.
# ######## [::-1] - satrni teskari qiladi
# with open('matn.txt', 'r') as file:
#     matn=file.read()
#     matn=matn.split()
# for soz in matn:
#     if soz == soz[::-1] and len(soz)>1:
#         print(soz)

# ### 7. Harf hisoblash
# Fayldagi har bir harf nechta kelganini hisobla.
###### .rstrip()- satrning (string) faqat oʻng tarafidagi (oxiridagi) boʻshliqlarni yoki koʻrsatilgan belgilarni olib tashlash uchun ishlatiladi.
###### .replace()- .replace() metodi satr (string) tarkibidagi biror bir belgini yoki soʻzni boshqasiga almashtirish uchun ishlatiladi
# with open('matn.txt', 'r') as file:
#     matn=file.read()
#     matn= matn.lower()
#     matn= matn.rstrip()
#     matn=matn.replace("\n", '')
#     matn=matn.replace(" ", '')
# kirit=input("Harf kiriting: ").lower()
# print(matn.count(kirit))

# # ### 8. Duplicate so‘zlar
# # Fayldagi takroriy so‘zlarni top.
# with open("matn.txt", "r") as file:
    # sozlar = file.read()
    # sozlar = sozlar.lower()
#     sozlar = sozlar.split()

# takroriy = set()
# for soz in sozlar:
#     if sozlar.count(soz) > 1:
#         takroriy.add(soz)
# print("Takroriy so'zlar:")
# for soz in takroriy:
#     print(soz)

# # ### 9. Eng ko‘p ishlatilgan so‘z
# # Faylda eng ko‘p uchragan so‘zni aniqlash.
# with open ('matn.txt', 'r') as file:
#     sozlar = file.read()
#     sozlar = sozlar.lower()
#     sozlar = sozlar.split()

# eng_kop=max(sozlar, key=sozlar.count)
# print('eng kup soz:', eng_kop)
# print('soni:', sozlar.count(eng_kop))

# ### 10. Faylni filter qilish
# Faqat 5 harfdan uzun so‘zlarni yangi faylga yoz.
with open('matn.txt', 'r') as file:
    sozlar = file.read()
    sozlar = sozlar.split()
with open('filter.txt', 'w') as fayl:
    for soz in sozlar:
        if len(soz) > 5:
            fayl.write(soz + '\n')