import time
import math
import os 
def addition(x,y):
    return x + y
def soustraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y 
def division(x,y):
    if y == 0:
        return("division par 0 impossible")
    return x / y
def nbaucarre(x):
    return x * x
def racinecarre(x):
    if x < 0:
        return "Impossible d'avoir la racine carre d'un nombre negatif !"
    return x **0.5
def nbaucube(x):
    return x ** 3
def puissance(x,y):
    return x ** y
def consinus(angle_degres):
    angle_radians = math.radians(angle_degres)
    return math.cos(angle_radians)

def tangente(angle_degres):
    angle_radians = math.radians(angle_degres)
    return math.tan(angle_radians)


while True:
    os.system('cls')
    print("\n--- Ma Calculatrice V1.2---")
    print("1: Addition")
    print("2: Soustraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Carre")
    print("6: Racine Carre")
    print("7: Cube")
    print("8: Puissance au choix")
    print("9: Cosinus")
    print("10: Tangente")
    print("11: Quitter")

    ReponseUser = input("Veuillez inserer une option entre 1 et 11: ")

    if ReponseUser == '11':
        print("Au revoir !")
        break

    if ReponseUser in ('1' '2' '3' '4'):
      try:
            num1 = float(input("Veuillez inserer le 1eme chiffre: "))
            num2 = float(input("Veuillez inserer le 2er chiffre: "))
        
      except ValueError:
        print("Erreur: veuillez inserer des chiffres valides")
        continue

    if ReponseUser == '1':
          print(f"voici le resultat {addition(num1, num2)}")

    if ReponseUser == '2':
        print(f"Voici le resultat {soustraction(num1, num2)}")
    
    if ReponseUser == '3':
        print(f"Voici le resultat {multiplication(num1, num2)}")

    if ReponseUser == '4':
        print(f"Voici le resultat {division(num1, num2)}")

    if ReponseUser in ('5' '6' '7'):
     try:
      num3 = float(input("Veuillez saisir votre nombre: "))
     except ValueError:
         print("Veuillez entrer un chiffre valide: ")
    if ReponseUser == '5':
         print(f"Voici votre nombre au carre {nbaucarre(num3)}")

    if ReponseUser == '6':
        print(f"Voici la Racine carre de votre nombre {racinecarre(num3)}")

    if ReponseUser == '7':
        print(f"Voici le cube de votre nombre {nbaucube(num3)}")

    if ReponseUser == '8':
        try:
         num4 = float(input("Par quel nombre voulez vous commencer ?: "))
         num5 = float(input("Vous voulez multiplier par quel puissance ?: "))
         print(f"Votre nombre puissance souhaiter {puissance(num4, num5)}")

        except ValueError:
            print("Veuillez inserer un nombre valide ")

    if ReponseUser == '9':
        try:
            angle = float(input("Entrez votre angle en degres: "))
            resultat = consinus(angle)
            print(f"La valeur du cosinus pour {angle} degres est {round(resultat, 4)}")
        except ValueError:
            print("Veuillez inserer un nombre valide !")

    if ReponseUser =='10':
        try:
            angle = float(input("Veuillez inserer votre angle en degres: "))
            resultat = tangente(angle)
            print(f"La valeur de la tangente pour {angle} degres est {round(resultat, 4)}")
        except ValueError:
            print("Veuillez inserer une donnee valide: ")

    if int(ReponseUser) < 1 or int(ReponseUser) > 11:
        try:
            print("Veuillez inserer un nombre inferieur a 11! ")
        except ValueError:
            print("Veuillez inserer un nombre valide ! ")
    
    print("Retour au menu dans 5 secondes")

    time.sleep(5)

