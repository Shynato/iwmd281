def carre(a):
    return a*a
def factorielle(a):
    i = 1
    result = 1
    while i < a+1:
        result = result * i
        i+=1
    return result
def exposant(a):
    i = 1
    result = a
    while i < a:
        result = result * a
        i+=1
    return result

choix = ""
while choix.upper() != "N":
    choixmenu = input("carre 1)\nfactorielle 2)\nexposant 3)\n")
    while True:
        try:
            nombre = int(input("indiquez le nombre:\n"))
            break
        except ValueError:
            print("Erreur ce n'est pas un nombre !")
    if choixmenu == "1":
        print(carre(nombre))
    elif choixmenu == "2":
        print(factorielle(nombre))
    elif choixmenu == "3":
        print(exposant(nombre))
    else:
        print("choix inconnu")
    choix = ""
    while choix.upper() != "N" and choix.upper() != "Y":
        choix = input("Continuer ? Y/N\n")
