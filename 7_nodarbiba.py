#Izstrādājat programmu, kurā lietotājs ievada kādu tekstu, un programma izvada - True, ja tekstā nav iekavas, vai iekavas ir aizvērtas. False, ja ir iekavas, kas nav aizvērtas. Padoms - Teksts praktiski ir saraksts ar burtiem!
# Piemērs:
# Ievade: (Hello!
# Izvada: False
# Ievade: (Hello)!
# Izvada: True
# Ievade: Hello!
# Izvada: True
# ievade = input("Teksts: ")
# atverosas_iekavas = 0
# aizverosas_iekavas = 0
# for burts in ievade:
#     if burts == "(":
#         atverosas_iekavas += 1
#     elif burts == ")":
#         aizverosas_iekavas += 1
# if atverosas_iekavas == aizverosas_iekavas:
#     print("True")
# else:
#     print("False")

# Funkcijas
# f(x) = ax^2 + bx + c
# f(x) = x ^ 2
# f(1) = 1 ^ 2
# f(2) = 2 ^ 2
def f(x :int) -> int:
    """
        Īss funkcijas apraksts
    """
    return x*x # return - atgriezt vērtību
print(f(2))
a = f(5)

def randint(a :int, b: int = 150) -> int:
    """
    Return random integer in range [a, b], including both end points.
    """
    print(a, b)
randint(0)

def pienem_sarakstu(a :'list[str]') -> None:
    print(a)
print(pienem_sarakstu([]))

import random
random.randint(0, 100)

# mainigais_funkc = 10
# def funkcijas():
#     # Jaunajās versijās ok - šī vērtība būs pieejama tikai zem šīs funkcijas
#     # Vecākās versijās - šeit tiks pārrakstīta 49 rindā nodefinētais mainīgais
#     mainigais_funkc = 25
#     print(mainigais_funkc)
# funkcijas()
# print(mainigais_funkc)
global_mainigais = 15   
def funkc_global():
    global global_mainigais # Ļauj izmainīt mainīgos, kas ir definēti ārpus funkcijas
    global_mainigais = 25
    print(global_mainigais)
    def funkcija_funkcijā(): # Nav pieejams no ārpuses - neiesaku tā darīt
        print("asd")
    funkcija_funkcijā()

funkc_global()
print(global_mainigais)
#funkcija_funkcijā()

def funkcija(*vairaki_parametri, parametra_nosaukums=""):
    print(vairaki_parametri[3])
    print(parametra_nosaukums)
funkcija(1,2,3,4, parametra_nosaukums="asd")
print("asd", "asd", end=" ")
print("Šis nebūs jaunā rindā")

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada lielāko skaitli
# Neizmantot iebūvētās python matemātiskās funkcijas (max())
def max_num(*saraksts):
    lielakais_skaitlis = saraksts[0]
    for iii in saraksts:
        if lielakais_skaitlis < iii:
            lielakais_skaitlis = iii
    return lielakais_skaitlis

lielakais_skaitlis = max_num(10,20,30,40,50)
print(lielakais_skaitlis)
print(max_num(100,20,90,40,50))

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada šo skaitļu reizinājumu
# Neizmantot iebūvētās python matemātiskās funkcijas (sum())
def reizinajums(*skaitli):
    reizinajums = 1
    for iii in skaitli:
        reizinajums *= iii
    return reizinajums

print(reizinajums(10, 20))
print(reizinajums(40,50,100))
mainigais = reizinajums(10, 20)
print(f"Rezultāts: {mainigais}")

# Rekursija: Funkcija, kas izsauc pati sevi:
# Piemērs: Funkcija izvada skaitļus no n (ievade) līdz 0 skaitot uz leju
def rekursija(parametrs):
    print(parametrs)
    if parametrs > 0:
        return rekursija(parametrs - 1)
    else:
        return parametrs # 0
rekursija(100)

# Faktoriālis - reizinājums visiem skaitļiem no 1 līdz n (piem 3! = 1*2*3=6)
# > Visu naturālo skaitļu no 1 līdz n reizinājumu sauc par skaitļa n faktoriālu un apzīmē n!
# 0!=1
#n = int(input("Ievadat skaitli: "))
n = 5
rezultats = 1
for skaitlis in range(1, n+1):
    print(f"{skaitlis}", end="*") # end="" - nākošais print paliks tajā pašā rindā
    rezultats *= skaitlis
print(f"={rezultats}")
# vai ar while ciklu
rezultats = 1
while n > 0:
    rezultats *= n
    n -= 1
print(rezultats)
# Uzdevums - uzrakstīt funkciju, kas rekursīvi aprēķina faktoriāli
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))