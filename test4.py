#Écrire un programme qui avec le nombre de marches d'un phare et la hauteur de chaque marche (en cm) données par l'utlisateur et qui renvoie une distance en m parcouru par le gardien 
# en 1 semaine de travail (5j)

m=float(input("Saisir le nombre de marche de votre phare: "))
h=float(input("Saisir la hauteur d'une marche en cm: "))
distance=m*h*4*5/100
print("La distance parcourue par le gardien est de",distance,"m")
    