#1-MASALA

# class SafeDivider:
#     def __get__(self, instance, owner):
#         try:
#             number = int(input("Son kiriting: "))
#             result = 100 / number
#             print(f"Natija: {result}")
#         except ZeroDivisionError:
#             print("❌ Nolga bo‘lish mumkin emas!")
#         except ValueError:
#             print("❗ Iltimos, to‘g‘ri butun son kiriting.")

# class DividerUser:
#     divide = SafeDivider()


# obj = DividerUser()
# obj.divide  


#2-MASALA

# import random

# try:
#     uzunlik = int(input("Ro'yxat uzunligini kiriting: "))
#     royxat = [f"Element-{i}" for i in range(uzunlik)]

#     tasodifiy_indeks = random.randint(0, uzunlik)  
#     print(f"Tanlangan indeks: {tasodifiy_indeks}")
#     print(f"Element: {royxat[tasodifiy_indeks]}")

# except IndexError:
#     print("❌ Bunday indeks mavjud emas!")
# except ValueError:
#     print("❗ Iltimos, butun son kiriting.")



#3-MASALA


# try:
#     qiymat = input("Iltimos, biror son kiriting: ")
#     son = int(qiymat)
#     print(f"✅ Siz kiritgan son: {son}")
# except ValueError:
#     print("❌ Noto‘g‘ri son!")



#4-MASALA

# try:
#     with open("ma'lumot.txt", "r") as fayl:
#         mazmun = fayl.read()
#         print("Fayl mazmuni:", mazmun)
# except FileNotFoundError:
#     print("Fayl topilmadi, yangi fayl yaratilmoqda...")
#     with open("ma'lumot.txt", "w") as yangi_fayl:
#         yangi_fayl.write("Bu yangi yaratilgan fayl.")
#     print("Yangi fayl yaratildi.")



#5-MASALA
# try:
#     son1 = int(input("birinchi sonni kiriting"))
#     son2 = int(input("ikkinchi sonni kiriting"))
#     def ayirma(son1, son2):
#         return son1 - son2
#     natija = ayirma(son1, son2)
#     print(natija)
# except ValueError:
#     print("iltimos son kiriting")

# finally:
#     print("dastur ishladi")


# 6-MASALA

# try:
#     boluvchi = int(input("Bo‘luvchini kiriting: "))
#     bolinuvchi = input("Bo‘linuvchini kiriting: ")

#     # Agar faqat son kiritilgan bo‘lsa (raqamlar), int ga aylantir
#     if bolinuvchi.isdigit():
#         bolinuvchi = int(bolinuvchi)
#     else:
#         raise ValueError("Bo‘linuvchi noto‘g‘ri kiritilgan")

# except ValueError as xato:
#     print(f"❌ Xatolik: {xato}")

# else:
#     try:
#         natija = boluvchi / bolinuvchi
#         print(f"✅ Natija: {natija}")
#     except ZeroDivisionError:
#         print("❗ Nolga bo‘lish mumkin emas!")





#7-MASALA

# ma_lumat = {
#     "ism": "Aziz",
#     "yosh": 25,
#     "shahar": "Toshkent"
# }

# try:
#     kalit = input("Qaysi kalitni kormoqchisiz? (masalan: ism, yosh, shahar): ")
#     qiymat = ma_lumat[kalit]
#     print(f"🔍 {kalit} = {qiymat}")
# except KeyError:
#     print("❌ Bunday kalit mavjud emas!")


#8-MASALA


# with open("sonlar.txt", "r") as fayl:
#     satrlar = fayl.readlines()

# for satr in satrlar:
#     satr = satr.strip()
#     try:
#         son = int(satr)
#         print(f"✅ Son: {son}")
#     except ValueError:
#         print("❌ Xato")





#9-masala


# lst = ["2", "3", "5", "4"]
# int_list = []
# for x in lst:
#     try:
#         int_list.append(int(x))
#     except ValueError:
#         print("xatolik bor")
#         break

# else:
#     print("hammasi tugri")


#10-MASALA

# my_list = []
# try:
#     if not my_list:
#         raise ValueError("bush")
#     summa = sum(my_list)
#     print(f"umumiy summa {summa}")

# except:
#     print("xatolik mavjud")

# else:
#     print("hammasi bajarildi")

# finally:
#     print("Dastur yakunlandi")





