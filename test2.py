#L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon.
n=int(input("Saisir un nombre entier: "))
if n<0:
    n=int(input("Saisir un nombre entier et POSITIF: "))
if n>=0:   
    if n%2==0:
        print("PAIR")
    else:
        print("IMPAIR")