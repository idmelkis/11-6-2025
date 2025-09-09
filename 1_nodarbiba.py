# CTRL + S
# Izmantojam F5 lai palaistu
# https://github.com/idmelkis/11-6-2025
"""
Vairāku
Rindu
Komentārs
"""
print("Izvade")
teksts = "Teksta vērtība"
# simbols = 'a'
skaitlis = 10
dalskaitlis = 10.0
patiesiba = True # False
#print(patiesiba)

saraksts = [123, "teksts", teksts]
print(saraksts[0]) # izvada pirmo (!) elementu - skaita no 0
print(saraksts[1])
print(saraksts[2])
saraksts[1] = "jaunā vērtība"
print(saraksts[1])
print(saraksts)
saraksts.append(-1) # Pievieno galā
print(saraksts)
saraksts.insert(1, "aaa") # Ievieto noteiktā vietā
print(saraksts)
saraksts.pop(0) # izdzēst no noteiktas vietas
print(saraksts)

# CTRL + K & (turot ctrl) C
# Komentē iezīmēto kodu
# ievade = input("Teksts kuru parāda prasot ievadi: ")
# print(ievade)

saraksts = [1,2,3,4]
print(saraksts[1:3]) # Izvada vērtības sākot no (pirms kola) līdz (pēc kola)
# ievade = input("Kaut kas: ")
# saraksts.append(ievade)
# print(saraksts)
teksts = f"123 {saraksts}"
print(saraksts)
