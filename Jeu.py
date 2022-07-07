import random

class Cringe_Morpion:
    def __init__(self):
        self.grille = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        class Joueur:
            def __init__(self, nom, score, numero):
                self.nom = nom
                self.score = score
                self.numero = numero
            def Ajouter_score(self, score):
                self.score += score
        self.joueurs = [Joueur("Joueur 1", 0, 1), Joueur("Joueur 2", 0, 2)]
        self.jouant = random.randint(0, 1)
        self.duree = 0
        self.gagnant = False

    def Afficher(self):
        for i in self.grille:
            print (i)
            print ()

    def Victoire(self):
        if self.gagnant == "egalite":
            print("Egalité")
            for i in self.joueurs:
                i.score += -50
        else:
            gagnant = self.joueurs[self.gagnant]
            perdant = self.joueurs[self.gagnant -1]
            gagnant.Ajouter_score(100)
            perdant.Ajouter_score(-100)
            print(gagnant.nom,"gagne son score est de",gagnant.score,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("duree:", self.duree)
            print("le score de", perdant.nom, "est de", perdant.score)
        self.Afficher()

    def Interface(self):
        print(self.joueurs[self.jouant].nom,":")
        self.Afficher()
        x = int(input("x: "))
        y = int(input("y: "))
        return x, y
    
    def Entre(self,x):
        return (0 <= x) and (x < 5)

    def Gagne(self, i, j, num):
        # on vérifie si le joueur a gagné
        if self.grille[i][j] == num:
            if self.Entre(j+2):
                if self.grille[i][j+2] == num and self.grille[i][j+1] == num:
                    return True
            if self.Entre(i+2):
                if self.grille[i+2][j] == num and self.grille[i+1][j] == num:
                    return True
            if self.Entre(j+2) and self.Entre(i+2):
                if self.grille[i+2][j+2] == num and self.grille[i+1][j+1] == num:
                    return True
            if self.Entre(j-2) and self.Entre(i+2):
                if self.grille[i+2][j-2] == num and self.grille[i+1][j-1] == num:
                    return True
    
    def Action(self, x, y):
        if self.grille[x][y] != 0:
            #si la case est déjà occupée, le joueur perd 1 point
            self.joueurs[self.jouant].Ajouter_score(-1)
            return
        self.grille[x][y] = self.joueurs[self.jouant].numero
        
        case_vide_restante = False
        for i in range(5):
            for j in range(5):
                if self.grille[i][j] == 0:
                    # on indique les cases ou l'on ne peut plus jouer
                    if not(x-2 <= i and i <= x+2) or not(y-2 <= j and j <= y+2):
                        self.grille[i][j] = 4
                    case_vide_restante = True
                
                if self.Gagne(i, j, self.joueurs[self.jouant].numero):
                    self.gagnant = self.jouant
                    return
                

        if not case_vide_restante:
            self.gagnant = "egalite"
    
    def Start(self):
        while self.gagnant == False:
            self.duree += 1

            x,y = self.Interface()

            self.Action(x,y)
            
            if self.jouant == 0:
                self.jouant = 1
            else:
                self.jouant = 0
        self.Victoire()


morpion = Cringe_Morpion()
morpion.Start()