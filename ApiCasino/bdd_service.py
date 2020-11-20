import pymysql.cursors


def get_bdd_connexion():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='ipssi_casino_g2',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def get_or_create_player(name_user, argent):
    try:
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:
            sql = """   SELECT * 
                        FROM joueur
                        WHERE pseudo = %s """        # gère automatiquement les failles injection sql
            cursor.execute(sql, (name_user))         # on exécute la requete avec les parametre rentré par le joueur
            row = cursor.fetchone()                  # on récupere le résulat
                                                     # %s = un parametre lambda
            if row is None:
                sql = """   INSERT INTO joueur(pseudo, argent)
                            VALUES (%s, %s)"""
                cursor.execute(sql, (name_user, argent))
                conn.commit()  # je valide les changements sur la bdd

            sql = """   SELECT id, pseudo, argent, YEAR(creation) as creation 
                        FROM joueur
                        WHERE pseudo = %s """
            cursor.execute(sql, (name_user))
            row = cursor.fetchone()

            print(f"Pseudo              : {row['pseudo']}")
            print(f"Argent              : {row['argent']}")
            print(f"Date de création    : {row['creation']}")

            row["max_lvl"] = get_max_niveau(row["id"])
            return row

    finally:
        conn.close()


def update_argent(id_joueur, argent):
    try:
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   UPDATE joueur
                        SET argent = %s 
                        WHERE id = %s """

            cursor.execute(sql, (argent, id_joueur))
            conn.commit()                               # je valide les changements sur la bdd

    finally:
        conn.close()


def add_new_resultat(id_joueur, niveau, victoire, nb_coup, mise, gain):
    try:
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   INSERT INTO resultat(id_joueur, niveau, victoire, nb_coup, mise, gain)
                            VALUES ( %s, %s, %s, %s, %s, %s)"""

            cursor.execute(sql, (id_joueur, niveau, victoire, nb_coup, mise, gain))
            conn.commit()                        # je valide les changements sur la bdd

    finally:
        conn.close()


def get_resultats(id_joueur):

    try :
        conn = get_bdd_connexion()
        with conn.cursor() as cursor:

            sql = """   SELECT * 
                        FROM resultat
                        WHERE id_joueur = %s"""

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
                print("")

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
            print(f"Nombre moyen de coup au niveau 3        : {row['moy_coup_vic_lvl3']}")

    finally:
        conn.close()


def get_max_niveau(id_joueur):
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
