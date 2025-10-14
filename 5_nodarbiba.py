# Komentējam: ctrl + /
# Uzdevums:
# Uzrakstīt programmu, kurā lietotājs ievada skaitli, un programma
# izvadīs rindas ar asteriskiem (*) - sākot ar vienu asterisku pirmajā
# rindā un par vienu vairāk katrā nākošajā
# piem. ievade 4
# Izvade:
# *
# **
# ***
# ****
# ievade = int(input("Skaitlis: "))
# for i in range(1, ievade + 1):
#     print(i * "*")
# # VAI
# skaititajs = 0
# while skaititajs < ievade:
#     skaititajs += 1
#     print(skaititajs * "*")


# % - atlikums
# print(10 % 2)

# Uzdevums:
# Uzrakstīt ciklu, kas iet pāri skaitļiem no 1 līdz 100, UN
# Ja skaitlis dalās ar 3, izvada vārdu "Fizz"
# Ja skaitlis dalās ar 5, izvada vārdu "Buzz"
# Attiecīgi, ja skaitlis dalās ar 3 un 5, izvada FizzBuzz
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, izvadat to
# Dalīšanas atlikuma pārbaudei izmatot - % - modulus operators
# Piem.
# 6 % 3 == 0 (dalās bez atlikuma)
# 7 % 3 == 1 (atlikums ir 1)
for sk in range(1, 101):
    if sk % 3 == 0 and sk % 5 == 0:
    #if sk % 15 == 0:
        print("FizzBuzz")
    elif sk % 3 == 0:
        print("Fizz")
    elif sk % 5 == 0:
        print("Buzz")
    else:
        print(sk)

# Spēle: Uzmini skaitli
# Uzdevums: Spēle "Uzmini skaitli"
# Spēle uzģenerē nejaušu skaitli izmantojot sekojošo kodu:
import random
skaitlis = random.randint(0, 100)

# Jāuzraksta cikls, kurā lietotājs ievada skaitli (input).
# Programma pārbauda vai skaitlis ir uzminēts,
# ja nav, izvada, vai ievadītais skaitlis ir lielāks, 
#  vai mazāks par nejaušo skaitli.
# Visas lietotāja ievades (minējumus) jāsaglabā sarakstā (.append())
# Kad lietotājs ir uzminējis skaitli - 
# Cikls beidzās, Izvadīt 'Uzvara', visus lietotāja minējumus