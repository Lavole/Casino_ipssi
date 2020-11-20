import os
import sys
import time
from random import randrange
from math import ceil
import bdd_service


# Déclaration des variables de départ
argent = 10                                                             # On a 10 € au début du jeu au niveau 1
continuer_partie = True                                                 # Booléen qui est vrai tant qu'on doit continuer la partie

print('Je suis Python. Quel est votre pseudo ?')                        # On demande a l'utilisateur de rentrer un pseudo


name_user = input()                                                     # Il va pouvoir le rentrer grâce a input.
print('Votre pseudo est', name_user,)                                   # On affiche le pseudo de l'utilisateur avec la variable name_user

joueur = bdd_service.get_or_create_player(name_user, argent)            # On crée la variable joueur et on appelle la fonction get_or_create_player qui se trouve dans bdd_service
id_joueur = joueur["id"]                                                # On défini que la variable id_joueur est bien id dans notre bdd
argent = joueur["argent"]                                               # On défini la variable argent comme quoi elle s'appel bien argent dans notre bdd

if argent <= 0:                                                         # SI argent est inférieur ou égal à 0 Alors
    print("Vous n'avez plus d'argent ")                                 # On affiche qu'il n'a plus d'agent
    print("Vous ne pouvez plus jouer")                                  # On affiche qu'il ne peut plus jouer

    voir_stat = input("Voulez vous voir vos statistiques (o/n)? ")      # On propose à l'utilisateur de voir ses statistiques
    if voir_stat == "o" or voir_stat == "O":                            # Si il répond o ou O Alors
        print("Voici vos statistiques.")                                # On lui écrit " Voici vos statistiques
        bdd_service.get_resultats(id_joueur)                            # En faisant appel a la fonction get_resultat dans bdd_services tout ca en fonction de l'id joueur
        bdd_service.get_resultats_moyenne(id_joueur)                    # En faisant appel a la fonction get_resultat moyen dans bdd_service tout ca en fonction de l'id joueur
    sys.exit()                                                          # On ferme le programme si il ne peut plus jouer

os.system("pause")

# On explique maintenant les règles du Casino :

print('Hello', name_user, f'vous avez {argent} €, Très bien ! Installez vous SVP à la table de pari. Je vous explique le principe du jeu : ')
print('Le jeu comporte 3 niveaux')
print("Le jeu comporte 3 levels avec la possibilié que le joueur choissise son level si ce n'est pas sa 1è fois dans le Casino. En d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint."
	"Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10), level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout) lors du 1è level, 5 au 2è level et 7 au 3è level. Chaque essai ne durera pas plus de 10 secondes. Au-delà,"
	"vous perdez votre essai. Att : si vous perdez un level, vous rejouez le level précédent. Quand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place. En absence de validation de la décision, le jeu est terminé.")
print('Pour le niveau 1 je vais tirer un nombre entre 1 et 10, vous allez devoir deviner ce nombre. ')


print('Bien', name_user, 'Vous vous installez au casino avec', argent, '€.')

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

                                                                        # on demande à l'utilisateur de saisir le nombre sur lequel il veut miser
    nb_user = -1
    gagne = False
    while nb_coup < chance_max and not gagne:
        print(nb_coup)
        nb_user = -1
        while nb_user < 0 or nb_user > max_range:
            nb_user = input(f"Tapez le nombre sur lequel vous voulez miser (entre 0 et {max_range}): ") #bdd_service.check_delais
            #if nb_user == False:
             #   break
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

             #   print("Mon choix est : ", nb_python) # pour voir le résultat de l'ordi
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

        voir_stat = input("Voulez vous voir vos statistiques (o/n)? ")  # On propose au joueur de visualiser ses statistiques
        if voir_stat == "o" or voir_stat == "O":                        # Si il répond o ou O Alors on affiche les stats
            print("Voici vos statistiques.")
            bdd_service.get_resultats(id_joueur)                        # On va chercher les stats dans la fonction get_resultats en fonction de l'id joueur
            bdd_service.get_resultats_moyenne(id_joueur)                # On va chercher les stats dans la fonction get_resultats_moyenne en fonction de l'id_joueur

        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")    # Si jamais il veut quitter le casino
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False                                    # On arrete la partie



# On met en pause le système (Windows)
os.system("pause")