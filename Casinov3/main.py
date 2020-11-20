import os
import sys
import time
from random import randrange
from math import ceil
import bdd_service


# Déclaration des variables de départ
argent = 10                                                             # On a 10 € au début du jeu au niveau 1
continuer_partie = True                                                 # Booléen qui est vrai tant qu'on doit continuer la partie

print(" *  *  *  *  *  *  *  *  *  *  * PROJET : REALISER UN JEU DE CASINO *  *  *  *  *  *  *  *  *  *  *\n\n")

name_user = input("Je suis Python. Quel est votre pseudo ? \n")

joueur = bdd_service.get_or_create_player(name_user, argent)            # On crée la variable joueur et on appelle la fonction get_or_create_player qui se trouve dans bdd_service
id_joueur = joueur["id"]                                                # On défini que la variable id_joueur est bien id dans notre bdd
argent = joueur["argent"]                                               # On défini la variable argent comme quoi elle s'appel bien argent dans notre bdd

if argent <= 0:                                                         # SI argent est inférieur ou égal à 0 Alors
    print("Vous n'avez plus d'argent ")                                 # On affiche qu'il n'a plus d'agent
    print("Vous ne pouvez plus jouer")                                  # On affiche qu'il ne peut plus jouer

    bdd_service.stats(id_joueur)
    sys.exit(0)                                                       # On ferme le programme si il ne peut plus jouer

os.system("pause")

# On explique maintenant les règles du Casino :

bdd_service.rules(name_user, argent)

print('\nBien', name_user, 'vous vous installez à la table avec', argent, '€.')

while continuer_partie:                                                 # Tant qu'on doit continuer la partie
                                                                        # On va maintenant configurer notre choix du lvl
    chance_max = 0                                                      # On défini différente variable
    nb_python = 0                                                       # On défini différente variable
    lvl = 0                                                             # On défini différente variable
    max_range = 0                                                       # On défini différente variable
    max_lvl = bdd_service.get_max_niveau(id_joueur)                     # On appel notre fonction get_max_lvl en fonction de l'id joueur dans notre bdd_service

    while lvl < 1 or lvl > max_lvl:                                     # Tant que le niveau choisi est inférieur au lvl 1 et supérieur au lvl Max alors
        lvl = input(f"Choississez votre niveau (1 à {max_lvl}) : ")     # On utilise la méthode format pour le f

        try:
            lvl = int(lvl)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")                    # Si vous saississez autre chose qu'un nombre
            lvl = 0
            continue
        if lvl < 1 or lvl > max_lvl:                                    # Si votre pseudo ne respecte pas la condition alors vous ne pouvez pas acceder a ce niveau
            print("Ce niveau n'existe pas")
                                                                        # On va maintenant définir le nombre de coup et la range radom pour chaque niveau
    if lvl == 1:                                                        # Pour le niveau 1
        chance_max = 3
        max_range = 10
    if lvl == 2:                                                        # Pour le niveau 2
        chance_max = 5
        max_range = 20
    if lvl == 3:                                                        # Pour le niveau 3
        chance_max = 7
        max_range = 30

    nb_python = randrange(max_range)                                    # Python tire maintenant le chiffre aléatoirement
    nb_coup = 0                                                         # Le nombre de coup démarrre a 0

                                                                        # À présent, on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        try:
            mise = int(mise)
        except ValueError:                                              # Si vous ne rentrer pas un nombre
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:                                                    # Si la mise est négative
            print("La mise saisie est négative ou nulle.")
        if mise > argent:                                               # Si on mise plus que ce que l'on a
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "€")

    nb_user = -1
    gagne = False
    while nb_coup < chance_max and not gagne:
        print(nb_coup)
        nb_user = -1
        while nb_user < 0 or nb_user > max_range:
            nb_user = bdd_service.check_delais(max_range)               # On demande a l'utilisateur de saisir sont choix en ne lui laissant que 10 sec

            # On convertit le nombre misé
            try:
                nb_user = int(nb_user)
            except ValueError:                                          # Si vous ne saississez pas de nombre
                print("Vous n'avez pas saisi de nombre")
                nb_user = -1
                continue
            if nb_user < 0:                                             # Si le nombre choisi est négatif
                print("Ce nombre est négatif")
            if nb_user > max_range:                                     # Si le nombre dépasse la Max range
                print(f"Ce nombre est supérieur à {max_range}")

                #print("Mon choix est : ", nb_python) # pour voir le résultat de l'ordi
        if nb_user != False:

            if nb_user == nb_python:                                    # Si on trouve le nombre
                print("gagné")
                gagne = True
            elif nb_user > nb_python:                                   # Si c'est trop grand
                print("trop grand")
            elif nb_user < nb_python:                                   # Si c'est trop petit
                print("trop petit")

        nb_coup += 1                                                    # On incrémente nb_coup par +1 a chaque fois qu'il essaye de trouver le nombre

                                                                        # Maintenant on établit le gain du joueur
    argent -= mise
    gain = 0
    victoire = True                                                     # On défini qu'il gagne

    if lvl == 1:                                                        # Pour le niveau 1
        if gagne and nb_coup == 1 :                                     # Il gagne en 1 coup
            gain = mise * 2                                             # Donc la mise est *2
            print("Félicitations ! Vous obtenez", gain, "€!")
            argent += gain                                              # On ajoute donc le gain a l'argent
        elif gagne and nb_coup == 2:                                    # Ils réussi au 2ème coup
            gain = mise                                                 # Donc il remporte juste sa mise
            print("Vous avez gagné au 2ème coup vous remportez votre mise : ", gain, "€")
            argent += gain                                              # On ajoute donc le gain a l'argent
        elif gagne and nb_coup == 3:                                    # Réussi au 3ème coup
            gain = ceil(mise * 0.5)                                     # Donc il remporte la moitié de sa mise
            print("Vous avez gagné au 3ème coup vous remportez la moitié de votre mise : ", gain, "€")
            argent += gain                                              # On ajoute donc le gain a l'argent
        else:
            print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
            victoire = False                                            # Si jamais il perd bah il gagne rien

    if lvl == 2:                                                        # Pour le niveau 2
        if gagne and (nb_coup == 1 or nb_coup == 2):                    # Il gagne en 1 ou 2 coups
            gain = mise * 2                                             # Donc la mise est *2
            print("Félicitations ! Vous obtenez", gain, "€!")
            argent += gain                                              # On ajoute donc le gain a l'argent
        elif gagne and (nb_coup == 3 or nb_coup == 4):                  # Ils réussi au 3 ou 4 eme coups
            gain = mise                                                 # Donc il remporte juste sa mise
            print("Vous avez gagné vous remportez votre mise : ", gain, "€")
            argent += gain                                              # On ajoute donc le gain a l'argent
        elif gagne and nb_coup == 5:                                    # Réussi au 5ème coup
            gain = ceil(mise * 0.5)                                     # Donc il remporte la moitié de sa mise
            print("Vous avez gagné vous remportez la moitié de votre mise : ", gain, "€")
            argent += gain                                              # On ajoute donc le gain a l'argent
        else:
            print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
            victoire = False                                             # Si jamais il perd bah il gagne rien

    if lvl == 3:                                                        # Pour le niveau 3
        if gagne and (nb_coup == 1 or nb_coup == 2 or nb_coup == 3):    # Il gagne en 1 2 ou 3 coups
            gain = mise * 2                                             # Donc la mise est *2
            print("Félicitations ! Vous obtenez", gain, "€!")
            argent += gain                                              # On ajoute donc le gain a l'argent
        elif gagne and (nb_coup == 4 or nb_coup == 5 or nb_coup == 6):  # Ils réussi au 5 ou 6 coup
            gain = mise                                                 # Donc il remporte juste sa mise
            print("Vous avez gagné vous remportez votre mise : ", gain, "€")
            argent += gain                                              # On ajoute donc le gain a l'argent
        elif gagne and nb_coup == 7:                                    # Réussi au 7ème coup
            gain = ceil(mise * 0.5)                                     # Donc il remporte la moitié de sa mise
            print("Vous avez gagné vous remportez la moitié de votre mise : ", gain, "€")
            argent += gain                                              # On ajoute donc le gain a l'argent
        else:
            print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
            victoire = False                                            # Si jamais il perd bah il gagne rien

    bdd_service.add_new_resultat(id_joueur, lvl, victoire, nb_coup, mise, gain)
    bdd_service.update_argent(id_joueur, argent)

    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", argent, "€")

        bdd_service.stats(id_joueur)
        continuer_partie = bdd_service.exit()

# On met en pause le système (Windows)
os.system("pause")