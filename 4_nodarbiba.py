# Uzdevums:
# Uzrakstat for ciklu, kas izvada skaitļus no 0 līdz 10, izlaižot skaitļus 4 un 6.
# for skaitlis in range(0,11):
#     if skaitlis != 4 and skaitlis != 6:
#         print(skaitlis)
    # if skaitlis == 4 or skaitlis == 6:
    #     continue
    # print(skaitlis)

# Uzdevums: Uzrakstīt šo for ciklu kā while ciklu
# skaitlis = -1
# while skaitlis < 10:
#     # if skaitlis != 4 and skaitlis != 6:
#     #     print(skaitlis)
#     # skaitlis += 1
#     skaitlis += 1
#     if skaitlis == 4 or skaitlis == 6:
#         continue
#     print(skaitlis)

# Uzdevums - uzrakstat ciklu (pēc izvēles) kas saskaita visas vērtības sarakstā,
# un jāizvada rezultāts. Neizmantot funkciju sum() (!).
# saraksts = [ 0, 5, 4, 10, 9 ]
# rezultats = 0
# for skaitlis in saraksts:
#     rezultats += skaitlis # rezultats = rezultats + skaitlis
# print(rezultats)

# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 1 līdz n (piem 3! = 1*2*3=6)
# > Visu naturālo skaitļu no 1 līdz n reizinājumu sauc par skaitļa n faktoriālu un apzīmē n!
# 0!=1
# n = int(input("Ievadat skaitli: "))
# rezultats = 1
# for skaitlis in range(1, n+1):
#     print(f"*{skaitlis}", end="") # end="" - nākošais print paliks tajā pašā rindā
#     rezultats *= skaitlis
# print(f"={rezultats}")
# Komentēšana - CTRL (jātur) + Slīpsvītra (/)

# Uzdevums: Izveidot 5x5 reizināšanas tabulu
# Hint - cikls ciklā, 2x for
# 1 2 3
# 2 4 6
# 3 6 9
rindas = 5
kolonas = 5
for rinda in range(1, rindas+1):
    for kolona in range(1, kolonas+1):
        print(f"{rinda*kolona}", end=" ")
    print()