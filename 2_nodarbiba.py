saraksts = [1,2,3,4]
teksts = f"123 {saraksts} {saraksts}" # Formatētā izvade - apvieno mainīgos iekš teksta (!)
print(saraksts)
mainigais = 2
print("Teksts", "Teksts 2", mainigais, "Teksts 3")
print("Teksts 1 " + str(mainigais)) # Neiesaku - saskaita vērtības

# Vairāku rindu izvade
print("""
Vairāku
Rindu
Komentārs
""")
print("Vairākas\nR\nindas") # (!)

print(b"\xff\xf8\x00\x00\x00\x00\x00\x00!") # Binārā izvade
print(u"😂🤣😍😒📙📙📙") # Unicode Izvade (nav obligāti - mūsdienās ir automātiski)
print(r"Vairākas\nR\nin\das\r") # Izvada simbolus bez apstrādes

#saraksts = [1,2,3,4]
saraksts = (1,2,3,4) # Tuple - nemaināms saraksts
# Piemērs - peles koordinātas - nav maināmas - ko izdod dators, tas ir - (x,y)

print(len("Teksts"))
print(len(["Teksts", "123"]))
print("Teksts"[2])
print(["Teksts", "123", "312"][2])
print("Teksts"[2:])

# ievade = input("Ievade: ")
# ievade2 = input("Ievade 2: ")
# print(int(ievade) + int(ievade2))

# if <pārbaude>:
#   ...

if True:
    print("Izpildās!")

mainīgais = 2
if mainīgais == 2:
    print("Izpildās")
if mainīgais is 2: # Alternatīva divām vienādojuma zīmēm
    print("Izpildās ar is")
if mainīgais == 3:
    print("neizpildās")
mainigais = mainīgais == 2
if mainigais:
    print(mainigais)

if not mainīgais == 3: # Not pārveido nākošās pārbaudes rezultātu - mainīgais NAV 3, bet not pārveido šo False par True.
    print("ASDASD")

if mainīgais > 5: # Nav vienāds ar
    print("ARQWEER")
elif mainigais < 2:
    print("ARQWEER")
else:
    print("Ne viens, ne otrs")
#if mainīgais <> 3: # Nav vienāds ar - Python 2 variants (redzēsiet tikai ļoti vecā kodā)
#    print("ARQWEER")

# ==, is - Vienāds
# not, != - Nav vienāds
# > - Lielāks par 3 > 2
# >= - Lielāks vai vienāds ar 2 >= 2
# < - Mazāks par 2 < 3
# <= Mazāks vai vienāds ar 2 <= 2

# Uzdevums 1: Izvada lietotāja ievadi
# Ievade: Cilvēka Vārds
# Izvade: Sveiks, <Vārds>!
vards = input("Ievadat vārdu: ")
# 3 Izvades varianti -
print(f"Sveiks, {vards}!")
print("Sveiks, ", vards, "!")
print("Sveiks, " + vards + "!")

# Uzdevums 2:
# Ievade: Skaitlis
# Izvade: "Jā", ja skaitlis ir lielāks par 10, "Nē" ja ir mazāks
skaitlis = int(input("Skaitlis: "))
if skaitlis > 10:
    print("Jā")
else:
    print("Nē")

# Uzdevums 3:
# Ievade: Jebkāds teksts
# Izvade: Šī teksta 1, 3 un 5 burts. Jāveic pārbaude vai ir tik garš teksts.
ievade = input("Ievade: ")
if len(ievade) >= 5:
    print(f"{ievade[0]} {ievade[2]} {ievade[4]}")