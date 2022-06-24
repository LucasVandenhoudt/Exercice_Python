#Conversion d'un nombre en chiffre romain
cr=""
n=int(input("Saisir le nombre que vous souahitez convertir en chiffre en romain: "))
while n >= 1000:
    cr += "M"
    n -= 1000
if n >= 900:
    cr += "CM"
    n -= 900
if n >= 500:
    cr += "D"
    n -= 500
if n >= 400:
    cr += "CD"
    n -= 400

while n >= 100:
    cr += "C"
    n -= 100
if n >= 90:
    cr += "XC"
    n -= 90
if n >= 50:
    cr += "L"
    n -= 50
if n >= 40:
    cr += "XL"
    n -= 40
while n >= 10:
    cr += "X"
    n -= 10
if n >= 9:
    cr += "IX"
    n -= 9
if n >= 5:
    cr += "V"
    n -= 5
if n >= 4:
    cr += "IV"
    n -= 4
while n >= 1:
    cr += "I"
    n -= 1

print (cr)    
