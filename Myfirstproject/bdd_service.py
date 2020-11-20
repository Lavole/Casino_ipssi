from threading import Thread
import pymysql.cursors
#from inputimeout import inputimeout, TimeoutOccurred

#answer = False
#msg = ""


#ef my_input():
    #global answer
# answer = input(msg)
#  return answer


#def check_delais(message):                                          # On créer la fonction check_delais pour le temps de 10 sec
    # Start bar as a process
# global answer
# answer = False
#  global msg
# msg = message
#  p = Thread(target=my_input)                                     # On crée un sous process qui permet au programme de tourner sur 2 trucs ( 2 thread)
#  p.start()

    # Wait for 10 seconds or until process finishes
#  p.join(11)

#  return answer


def get_bdd_connexion():                                                # On créer la fonction get_bdd_connexion qui va nour permettre de nous connecter a la bdd

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='ipssi_casino_g2',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor) # On va donc se connecter en local (avec Wampserver sur phpmyadmin)
    return connection


def get_or_create_player(name_user, argent):                            # On créer la fonction get_or_create_player
    try:
        conn = get_bdd_connexion()                                      # On défini la variable conn qui nous permet de nous connecter a la bdd en prenant le get_bdd_connexion
        with conn.cursor() as cursor:
            sql = """   SELECT * 
                        FROM joueur
                        WHERE pseudo = %s """                           # On affiche toutes les données de la table joueur en fonction de pseudo rentré
                                                                        # gère automatiquement les failles injection sql
            cursor.execute(sql, (name_user))                            # on exécute la requete avec les parametre rentré par le joueur
            row = cursor.fetchone()                                     # on récupere le résulat
                                                                        # %s = un parametre lambda
            if row is None:                                             # Si jamais on ne retrouve pas le pseudo alors on va faire une requete SQL pour le crée
                sql = """   INSERT INTO joueur(pseudo, argent)
                            VALUES (%s, %s)"""                          # La requete SQL pour créer le joueur avec son argent de départ aka 10 euros
                cursor.execute(sql, (name_user, argent))
                conn.commit()                                           # je valide les changements sur la bdd

            sql = """   SELECT * 
                        FROM joueur
                        WHERE pseudo = %s """                           # Du coup on affiche encore pour le pseudo
            cursor.execute(sql, (name_user))
            row = cursor.fetchone()

            print(f"Pseudo              : {row['pseudo']}")             # Et on peut afficher les données aka Pseudo argent ainsi que date de création
            print(f"Argent              : {row['argent']}")
            print(f"Date de création    : {row['creation']}")

            return row

    finally:
        conn.close()


def update_argent(id_joueur, argent):
    try:
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   UPDATE joueur
                        SET argent = %s 
                        WHERE id = %s """                               # Requete Sql pour update l'agent

            cursor.execute(sql, (argent, id_joueur))
            conn.commit()                                               # je valide les changements sur la bdd

    finally:
        conn.close()


def add_new_resultat(id_joueur, niveau, victoire, nb_coup, mise, gain):
    try:
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   INSERT INTO resultat(id_joueur, niveau, victoire, nb_coup, mise, gain)
                            VALUES ( %s, %s, %s, %s, %s, %s)"""         # On insert les données dans la bdd

            cursor.execute(sql, (id_joueur, niveau, victoire, nb_coup, mise, gain))
            conn.commit()                                                # je valide les changements sur la bdd

    finally:
        conn.close()


def get_resultats(id_joueur):

    try :
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   SELECT * 
                        FROM resultat
                        WHERE id_joueur = %s"""                         # Avec les données inséré précédemment on peut tout affichier avec un select

            cursor.execute(sql, (id_joueur))
            rows = cursor.fetchall()

            for row in rows:
                print(f"Numéro de jeu            : {row['id']} ")
                print(f"Niveau                   : {row['niveau']}")
                print(f"Victoire                 : {bool(row['victoire'])}")
                print(f"Nombre de coup           : {row['nb_coup']}")
                print(f"Mise                     : {row['mise']}")
                print(f"Gain                     : {row['gain']}")
                print(f"Date du jeu              : {row['creation']}")
                print("")                                               # Du coup on affiche les statistiques pour chaque partie ( lien dans main)

    finally:
        conn.close()


def get_resultats_moyenne(id_joueur):

    try:
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   SELECT 
                            COUNT(*) as nb_result,
                            AVG(gain) as sum_gain, 
                            AVG(mise) as sum_mise,
                            (SELECT COUNT(*) FROM resultat WHERE id_joueur = %(id_joueur)s AND victoire = 1) as nb_vic,
                            (SELECT COUNT(*) FROM resultat WHERE id_joueur = %(id_joueur)s AND victoire = 0) as nb_def,
                            (SELECT AVG(nb_coup) FROM resultat WHERE id_joueur = %(id_joueur)s AND victoire = 1) as moy_coup_vic,
                            (SELECT AVG(nb_coup) FROM resultat WHERE id_joueur = %(id_joueur)s AND victoire = 1 AND niveau = 1) as moy_coup_vic_lvl1,
                            (SELECT AVG(nb_coup) FROM resultat WHERE id_joueur = %(id_joueur)s AND victoire = 1 AND niveau = 2) as moy_coup_vic_lvl2,
                            (SELECT AVG(nb_coup) FROM resultat WHERE id_joueur = %(id_joueur)s AND victoire = 1 AND niveau = 3) as moy_coup_vic_lvl3
                        FROM resultat
                        WHERE id_joueur = %(id_joueur)s"""

            cursor.execute(sql, {"id_joueur": id_joueur})                   # partout ou il y a Id_joueur il va chercher id_joueur = dictionnaire
            row = cursor.fetchone()                                         # as permet de renomer la colonne

            print(f"Nombre de victoire                      : {row['nb_vic']}")
            print(f"Nombre de défaite                       : {row['nb_def']}")
            print(f"Nombre moyen de coup                    : {row['moy_coup_vic']}")
            print(f"Nombre moyen de coup au niveau 1        : {row['moy_coup_vic_lvl1']}")
            print(f"Nombre moyen de coup au niveau 2        : {row['moy_coup_vic_lvl2']}")
            print(f"Nombre moyen de coup au niveau 3        : {row['moy_coup_vic_lvl3']}")      # du coup on affiche

    finally:
        conn.close()


def get_max_niveau(id_joueur):                                              # On défini maintenant le niveau max en fonction de l'id joueur
    try :
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   SELECT MAX(niveau) as max_lvl
                        FROM resultat
                        WHERE id_joueur = %s"""

            cursor.execute(sql, (id_joueur))
            row = cursor.fetchone()

            if row["max_lvl"] is None:
                return 1
            elif row["max_lvl"] == 3:
                return row["max_lvl"]
            else:
                return row["max_lvl"]+1
    finally:
        conn.close()
