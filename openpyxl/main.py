# from openpyxl import Workbook

# wb = Workbook()
# ws = wb.active

# ws["A1"] = "Ism"
# ws["B1"] = "Yosh"

# ws["A2"] = "Ali"
# ws["B2"] = 20

# wb.save("talabalar.xlsx")

# print("Excel fayl yaratildi!")

# from openpyxl import Workbook

# wb = Workbook()
# ws = wb.active

# ws["A1"] = "Ism"
# ws["B1"] = "Yosh"

# for i in range(2, 11):
#     ws[f"A{i}"] = "Alibek"
#     ws[f"B{i}"] = 20

# wb.save("talabalar.xlsx")

# print("Excel fayl yaratildi!")
################################################ 📊 openpyxl — 10 EASY ##############################
# from openpyxl import Workbook, load_workbook
# # 1. Excel yaratish
# # students.xlsx fayl yarat.
# wb = Workbook()
# wb.save("students.xlsx")

# # 2. Ma’lumot yozish
# # 1 ta student ma’lumotini yoz.
# wb=Workbook()
# ws=wb.active
# ws['A1']='Ism'
# ws['B1']='Familya'

# ws['A2']='Alibek'
# ws['B2']='Nosiraliyev'

# wb.save("students.xlsx")

# # 3. 3 ta student yozish
# # Excelga 3 ta student qo‘sh.
# wb=Workbook()
# ws=wb.active

# ws['A1']='Ism'
# ws['B1']='Familya'

# ws['A2']='Alibek'
# ws['B2']='Nosiraliyev'

# ws['A3']='Shodiyor'
# ws['B3']='Baxtiyorov'

# ws['A4']='Azizjon'
# ws['B4']='Abdiyoqupov'

# wb.save("students.xlsx")

# # 4. Faylni ochish
# # Mavjud Excelni o‘qish.
# wb = load_workbook("students.xlsx")
# ws = wb.active

# print("Excel fayl bor")

# # 5. Cell o‘qish
# # A1 katakdagi qiymatni chiqar.
# wb= load_workbook("students.xlsx")
# ws= wb.active

# print(ws['A1'].value)

# # 6. Sheet nomi
# # Sheet nomini chiqar.
# ### ws.title → aktiv sheet nomini qaytaradi.
# wb= load_workbook("students.xlsx")
# ws= wb.active

# print(ws.title)

# # 7. Yangi sheet qo‘shish
# # Yangi sheet yarat.
# wb= load_workbook("students.xlsx")
# ws= wb.active
# ws1=wb.active
# ws1= wb.create_sheet('Talabalar')

# wb.save('students.xlsx')

# # 8. Ustun yozish
# # Ism, Yosh, Ball ustunlarini yoz.
# wb=load_workbook("students.xlsx")
# ws=wb.active
# ws.title = "Talabalar"

# ws["A1"] = "Ism"
# ws["B1"] = "Yosh"
# ws["C1"] = "Ball"

# wb.save("students.xlsx")

# # 9. Row soni
# # Nechta qator borligini chiqar.
# #### qatorlar sonini sanash uchun max_row ishlatiladi.
# wb= load_workbook("students.xlsx")
# ws= wb.active

# print(ws.max_row)

# # 10. Excelni saqlash
# # O‘zgartirilgan faylni save qilish.
# wb = load_workbook("students.xlsx")

# wb.save("students.xlsx")
# print("Yangi fayl saqlandi.")

################################################ 📊 openpyxl — 10 MEDIUM ######################################
from openpyxl import Workbook, load_workbook
# ### 1. O‘rtacha ball
# Exceldagi ballarning o‘rtachasini hisobla.
# wb = load_workbook("students.xlsx")
# ws = wb.active
# jami = 0
# soni = 0
# for row in range(2, ws.max_row + 1):
#     ball = ws[f"C{row}"].value
#     print(ball)
#     if ball is not None:
#         jami += ball
#         soni += 1
# print("O'rtacha ball:", jami / soni)

# ### 2. Filter (80+)
# Balli 80 dan yuqori studentlarni chiqar.
# wb = load_workbook('students.xlsx')
# ws=wb.active
# for row in range(2, ws.max_row + 1):
#     ball = ws[f"C{row}"].value
#     if ball > 80:
#         name = ws[f"A{row}"].value
#         print(name)
        
# ### 3. Status ustuni
# Ballga qarab A’lo / Yaxshi / Qoniqarsiz yoz.
# wb = load_workbook('students.xlsx')
# ws=wb.active
# ws['D1']="Status"
# for row in range(2, ws.max_row + 1):
#     ball = ws[f"C{row}"].value
#     if ball >= 90:
#         ws[f"D{row}"]="A'lo"
#     elif ball >=70 and ball < 90:
#         ws[f"D{row}"]="Yaxshi" 
#     else:
#         ws[f"D{row}"]="Qoniqarsiz"

# wb.save('students.xlsx')
        
# ### 4. Eng yuqori ball
# Eng yuqori ball egasini top.
# wb = load_workbook('students.xlsx')
# ws=wb.active
# ws['D1']="Status"
# eng_yuqori_ball = 0
# eng_yaxshi_talaba = ""
# for row in range(2, ws.max_row + 1):
#     ball = ws[f"C{row}"].value
#     if ball > eng_yuqori_ball:
#         eng_yuqori_ball = ball
#         eng_yaxshi_talaba = ws[f"A{row}"].value
# print("Eng yaxshi talaba:", eng_yaxshi_talaba)
# print("Ball:", eng_yuqori_ball)

# ### 5. Sorting
# Ball bo‘yicha kamayish tartibida qayta yoz.
# wb = load_workbook('students.xlsx')
# ws = wb.active

# ballar = []
# for row in ws.iter_rows(min_row=2, values_only=True):
#     ballar.append(row)
# ballar.sort(key=lambda x: x[2], reverse=True)
# print(ballar) 

# ### 6. Yangi sheetga ko‘chirish
# 80+ studentlarni yangi sheetga yoz.

# ### 7. Column qo‘shish
# “Grade” ustunini qo‘sh.
# wb = load_workbook("students.xlsx")
# ws = wb.active
# new_col = ws.max_column + 1
# ws.cell(row=1, column=new_col).value = "Grade"
# wb.save("students.xlsx")

# ### 8. Excelni tozalash
# Bo‘sh qatorlarni o‘chir.

# # ### 9. Statistik hisobot
# # min, max, avg hisobla.
# wb = load_workbook('students.xlsx')
# ws = wb.active

# ballar = []
# jami=0
# soni=0

# for row in range(2, ws.max_row + 1):
#     ballar.append(ws[f"C{row}"].value)

# for i in ballar:
#     jami+=i
#     soni+=1

# print(ballar)
# print("Eng kichkina son:", min(ballar))
# print("Eng katta son:", max(ballar))
# print("O'rtacha ball:", jami / soni)

# ### 10. Excel → TXT export
# Excel ma’lumotini txt faylga o‘tkaz.
