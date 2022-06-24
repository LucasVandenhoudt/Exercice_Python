def fizzbuzz():
    n1=int(input("Saisir le premier nombre: "))
    n2=int(input("Saisir le deuxième nombre: "))
    for nb in range (1,101):
        if nb%n1==0 and nb%n2==0:
            print("FizzBuzz")
        elif nb%n2==0:
            return "Buzz"
        elif nb%n1==0:
            print("Fizz")
        else:
            print(nb)


