import math
mainigais = 10
mainigais2 = [ 123, 45 ]

print("Kaut kas")
print("Kaut kas")
print("Kaut kas")
mainigais = 20
print("Kaut kas")
# Kļūdu pārķeršana: https://docs.python.org/3/tutorial/errors.html
# Saraksts ar visām kļūdām, ko Python var izmest: https://docs.python.org/3/library/exceptions.html
try:
    #raise Exception("123") # Izmest pašiem savu kļūdu ar pašiem savu vērtību
    #print("Nav kļūda")
    a = "1" + 1
except TypeError:
    print("Kļūda ar datu tipiem")
except Exception as e:
    # Izvadam kļūdas ziņojumu
    print(e)
except:
    print("Cita kļūda")

def funkcija():
    # Parādās call stack
    nosaukums = 90 
    print(nosaukums)
funkcija()

for i in range(0, 90):
    a = i + 2
    b = a / 3
    print(b)