from tkinter import *
from helper import *
from de import De


class GameTextureLoader:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arene_bg = resize_image("arena.png", self.width, self.height)


class Arene:

    def __init__(self, master, dimension, de_initial, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.dimension = dimension
        self.textures = GameTextureLoader(self.width, self.height)
        self.arene_canvas = Canvas(self.master, width=self.width, height=self.height)

        self.arene_tile = resize_image("tile.png", self.width//32, self.height//18)

        de_initial.lancer()
        while de_initial.valeur == 1:
            de_initial.lancer()
        self.coordonnees = {}
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.coordonnees[(i, j)] = None
        self.coordonnees[(self.dimension // 2, self.dimension // 2)] = de_initial

    def dans_arene(self, emplacement):
        """
        Vérifie si un emplacement est inclus dans l'arène.
        Un emplacement (x, y) est dans l'arène s'il se trouve entre (0,0)
        et (d-1, d-1) inclusivement, où d est la dimension de l'arène

        Args:
            emplacement ((int, int)): Coordonnées dont on veut vérifier l'inclusion

        Returns:
            bool: True si l'emplacement est dans l'arène, False sinon
        """
        # VOTRE CODE ICI
        emplacement_x = emplacement[0]
        emplacement_y = emplacement[1]
        return emplacement_x in range(0, self.dimension) and emplacement_y in range(0, self.dimension)

    def effectuer_lancer(self, lancer):
        """
        Obtient la trajectoire du lancer (Lancer.trajectoire), relance les
        dés accrochés (Arene.relancer_des_accroches) au passage pour tous les
        emplacements de la trajectoire excepté le dernier, puis place le dé du
        lancer au dernier emplacement de la trajectoire (Arene.placer_nouveau_de).

        Args:
            lancer (Lancer): contient les informations sur le lancer à effectuer
        """
        # VOTRE CODE ICI
        self.relancer_des_accroches(lancer.trajectoire)
        emplacement_final = lancer.trajectoire[-1]
        self.placer_nouveau_de(lancer.de, emplacement_final)

    def relancer_des_accroches(self, trajectoire):
        """
        Pour chaque emplacement de la trajectoire, relancer le dé (De.lancer) qui
        se trouve à cet emplacement, s'il y en a un.

        Args:
            trajectoire (list): Liste des coordonnées où l'on doit relancer
        """
        # VOTRE CODE ICI
        for emplacement in trajectoire:
            if emplacement in list(self.coordonnees.keys()):
                self.coordonnees[emplacement].lancer()

    def placer_nouveau_de(self, de, emplacement_final):
        """
        Si l'emplacement final est dans l'arène (Arene.dans_arene),
        on lance le dé (De.lancer) et on l'ajoute dans le dictionnaire de dés
        à l'emplacement final.

        Important: Si un dé est déjà présent à cet emplacement, ce dernier est retiré
        pour laisser place au nouveau dé.

        Args:
            de (De): Le dé à ajouter
            emplacement_final ((int, int)): Les coordonnées où ajouter le dé
        """
        # VOTRE CODE ICI
        if self.dans_arene(emplacement_final):
            de.lancer()
            self.coordonnees[emplacement_final] = de

    def effectuer_plusieurs_lancers(self, liste_lancers):
        """
        Effectue chaque lancer (Arene.effectuer_lancer) de la liste de lancers.

        Args:
            liste_lancers (list): La liste de lancers à effectuer
        """
        # VOTRE CODE ICI
        for lancer in liste_lancers:
            self.effectuer_lancer(lancer)

    def rangement(self, joueur_en_cours):
        """
        Il s'agit d'enlever les dés de l'arène, suivant les règles du jeu:
          - On retire d'abord tous les X (Arene.retirer_les_x)
          - On compte combien des autres valeurs sont présentes (Arene.compter_valeurs)
          - On retire les dés non uniques (Arene.retirer_correspondances)
        On retourne ensuite un booléen indiquant si une correspondance
        a eu lieu (Arene.correspondance_existe)

        Args:
            joueur_en_cours (Joueur): le joueur qui vient de lancer

        Returns:
            bool: True si une correspondance a eu lieu, False sinon.
        """
        # VOTRE CODE ICI
        self.retirer_les_x()
        self.compter_valeurs()
        self.retirer_correspondances(self.compter_valeurs(), joueur_en_cours)
        if self.correspondance_existe(self.compter_valeurs()):
            return True
        else:
            return False

    def retirer_les_x(self):
        """
        Parmi toutes les entrées du dictionnaire de dés, retire
        (Arene.retirer_de) celles dont la valeur est 1.

        Astuce: commencez par identifier les emplacements avec les X en les mettant
        dans une liste, puis retirez-les dans un deuxième temps, car faire des suppressions
        dans un dictionnaire en même temps que l'on itère dessus est déconseillé.
        """
        # VOTRE CODE ICI
        emplacement_liste = []
        for emplacement, de in self.coordonnees.items():
            if de.valeur == 1:
                emplacement_liste.append(emplacement)
        for emplacement in emplacement_liste:
            self.retirer_de(emplacement)

    def compter_valeurs(self):
        """
        Retourne un dictionnaire associant les numéros 2, 3, 4, 5 et 6
        au nombre de dés ayant ces valeurs.

        Exemple: si l'arène contient 3 dés (un 5 et deux 3),
        alors on retourne {2:0, 3:2, 4:0, 5:1, 6:0}

        Returns:
            dict: Le dictionnaire associant valeurs de dés et nombre d'occurence
        """
        # VOTRE CODE ICI
        comptes = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for de in self.coordonnees.values():
            if not de.valeur == 'X':
                comptes[de.valeur] += 1
        return comptes

    def retirer_correspondances(self, comptes, joueur_en_cours):
        """
        Parmi toutes les entrées du dictionnaire de dés, rend au joueur
        (Arene.rendre_au_joueur) celles dont la valeur est présente plus d'une fois.

        Astuce: commencez par identifier les emplacements des dés à enlever en les mettant
        dans une liste, puis retirez-les dans un deuxième temps, car faire des suppressions
        dans un dictionnaire en même temps que l'on itère dessus est déconseillé.

        Args:
            comptes (dict): Nombre d'occurences de chaque valeur de dé
            joueur_en_cours (Joueur): le joueur à qui rendre les dés

        """
        # VOTRE CODE ICI
        liste_emplacement = []
        for emplacement, de in self.coordonnees.items():
            if comptes[de.valeur] > 1:
                liste_emplacement.append(emplacement)
        for emplacement in liste_emplacement:
            self.rendre_au_joueur(emplacement, joueur_en_cours)

    def correspondance_existe(self, comptes):
        """
        Indique s'il existe une valeur présente plus d'une fois sur l'arène.

        Args:
            comptes (dict): Un dictionnaire indiquant, pour chaque valeur
                de dé de 2 à 6, combien sont présents sur l'arène.

        Returns:
            bool: True si une valeur de dé est là plus d'une fois, False sinon.
        """
        # VOTRE CODE ICI
        for i in comptes.values():
            if i > 1:
                return True
        return False

    def est_vide(self):
        """
        Vérifie si l'arène est vide.

        Returns:
            bool: True si aucun dé n'est présent, False sinon.
        """
        # VOTRE CODE ICI
        if self.coordonnees == {}:
            return True
        else:
            return False

    def retirer_de(self, emplacement):
        """
        Retire un dé définitivement. Utilisez le mot-clé del.

        Args:
            emplacement ((int, int)): L'emplacement du dé à éliminer.
        """
        # VOTRE CODE ICI
        del self.coordonnees[emplacement]

    def rendre_au_joueur(self, emplacement, joueur):
        """
        Rend le dé situé à l'emplacement au joueur (Joueur.rendre_de),
        et retire le dé de l'arène (Arene.retirer_de). L'ordre des appels est important!

        Args:
            emplacement ((int, int)): L'emplacement du dé à rendre
            joueur (Joueur): Le joueur à qui rendre le dé
        """
        # VOTRE CODE ICI
        joueur.rendre_de(self.coordonnees[emplacement])
        self.retirer_de(emplacement)

    def afficher_de(self):
       pass

    def affichage_arene(self, Lancer=None):
        self.arene_canvas.create_image(0, 0, image=self.textures.arene_bg, anchor="nw")
        for (i, j) in self.coordonnees.keys():
            self.arene_canvas.create_image(775+(100*i), 300+(100*j), image=self.arene_tile, anchor="center")
        self.arene_canvas.pack(fill="both", expand=True)


if __name__ == "__main__":
    window = Tk()
    window.geometry("1920x1080")
    arene = Arene(window, 5, De(), 1920, 1080)
    arene.affichage_arene()
    de_test = De()
    arene.affichage_arene()
    window.mainloop()
