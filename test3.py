#L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.
n=int(input("Saisir un nombre entier: "))
if n<0:
    n=int(input("Saisir un nombre entier et positif: "))
compteur=0
while n%2==0:
    n=n//2
    compteur=compteur+1
print ("Ce nombre est divise par 2",compteur," ","fois")
