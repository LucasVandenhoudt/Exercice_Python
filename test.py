#Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
from math import pi
rayon=float(input("Saisir un rayon: "))
hauteur=float(input("Saisir une hauteur: "))
volume=(rayon*rayon*hauteur*pi)/3
Volume=round(volume,2)
print("Le volume du cône est de",Volume,"cm3")


