# Uzdevums: Kalkulators
# Ievade: Divi skaitļi, darbība
# (saskaitīšana, atņemšana, dalīšana un
# reizināšana)
# Izvade: Darbības rezultāts
# skaitlis_1 = float(input("Ievadat pirmo skaitli"))
# skaitlis_2 = float(input("Ievadat otro skaitli"))
# darbiba = input("Darbība: ")
# if darbiba == "+":
#     print(f"Rezultāts: {skaitlis_1+skaitlis_2}")
# elif darbiba == "-":
#     print(f"Rezultāts: {skaitlis_1-skaitlis_2}")
# elif darbiba == "/":
#     print(f"Rezultāts: {skaitlis_1/skaitlis_2}")
# elif darbiba == "*":
#     print(f"Rezultāts: {skaitlis_1*skaitlis_2}")
# else:
#     print("Neatpazīta darbība")

# switch/match - praktiski if ar vienāds ar darbību, atbalstīts tikai ar python 3.10+
# match darbiba:
#     case "+":
#         print(f"Rezultāts: {skaitlis_1+ skaitlis_2}")
#     case "-":
#         print(f"Rezultāts: {skaitlis_1-skaitlis_2}")
#     case "/":
#         print(f"Rezultāts: {skaitlis_1/skaitlis_2}")
#     case "*":
#         print(f"Rezultāts: {skaitlis_1*skaitlis_2}")
#     case _:
#         print("Neatpazīta darbība")

# for
# while
# For - Iet pāri kādam sarakstam
# for i in [1,2,3,4]:
#     print(i)
for i in range(0,10):
    print(i)
# While - izpildās kamēr nosacījums ir patiess
skaitlis = 0
while skaitlis < 10:
    print(skaitlis)
    skaitlis += 1

# saraksts = [1,2,3,4]
# indekss = 0
# beidza = False

# while True:
#     if not beidza:
#         #while not indekss == len(saraksts): 
#         while indekss < len(saraksts): # zem while iet loģiskās pārbaudes - tādas pašas kādas zem if
#             print(saraksts[indekss])
#             indekss += 1
#             if indekss == 2:
#                 beidza = True
#                 break # Beidz tekošā cikla darbību
#         print("Cikls2 beidza darbu")
#     else:
#         print("Cikls1 beidza darbu")
#         break

a = 0
while a < 10:
    a += 1
    if a == 5:
        continue # Izlaiž visu PĒC šī continue
    print(a)

# Piemērs - meklējam vērtību ciklā (ar for)
meklējamā_vērtība = 5
saraksts = [ 0, 1, 3, 5, 7, 2]
atrastais_indekss = -1
for i in range(0, len(saraksts)):
    print(f"Cikls darbojās {i} reizes")
    if saraksts[i] == meklējamā_vērtība:
        atrastais_indekss = i
        break
print(atrastais_indekss)

# Uzdevums: uzrakstīt for ciklu, kas ļauj lietotājam ievadīt sarakstā 3 vērtības
saraksts = []
for i in range(3):
    saraksts.append(input("Ievade: "))
print(f"Ievadīts: {saraksts}")
#print("Ievadīts:", saraksts)
# Uzdevums: Uzrakstīt šo darbību ar while ciklu
saraksts = []
indekss = 0
while indekss < 3:
    saraksts.append(input("Ievade: "))
    indekss += 1
print(f"Ievadīts: {saraksts}")

# VAI
saraksts = []
while len(saraksts) < 3:
    saraksts.append(input("Ievade: "))
print(f"Ievadīts: {saraksts}")



# ...2D


