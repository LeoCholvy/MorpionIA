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
            for i in self.joueurs:
                if i != self.gagnant:
                    perdant = i
            perdant.Ajouter_score(-100)
            self.gagnant.Ajouter_score(100)
            print(self.gagnant.nom,"gagne son score est de",self.gagnant.score,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("duree:", self.duree)
            print("score perdant:", perdant.score)
        self.Afficher()

    def Interface(self):
        print(self.joueurs[self.jouant].nom,":")
        self.Afficher()
        x = int(input("x: "))
        y = int(input("y: "))
        return x, y
    
    def Entre(self,x):
        return (0 <= x) and (x < 5)

    
    def Action(self, x, y):
        if self.grille[x][y] != 0:
            return
        self.grille[x][y] = self.joueurs[self.jouant].numero
        
        case_vide_restante = False
        for i in range(5):
            for j in range(5):
                if self.grille[i][j] == 0:
                    if not(x-2 <= i and i <= x+2) or not(y-2 <= j and j <= y+2):
                        self.grille[i][j] = 4
                    case_vide_restante = True
                
                num = self.joueurs[self.jouant].numero
                if self.grille[i][j] == num:
                    if self.Entre(j+2):
                        if self.grille[i][j+2] == num and self.grille[i][j+1] == num:
                            self.gagnant = self.joueurs[self.jouant]
                            return
                    if self.Entre(i+2):
                        if self.grille[i+2][j] == num and self.grille[i+1][j] == num:
                            self.gagnant = self.joueurs[self.jouant]
                            return
                    if self.Entre(j+2) and self.Entre(x+2):
                        if self.grille[i+2][j+2] == num and self.grille[i+1][j+1] == num:
                            self.gagnant = self.joueurs[self.jouant]
                            return
                    if self.Entre(j-2) and self.Entre(x+2):
                        if self.grille[i+2][j-2] == num and self.grille[i+1][j-1] == num:
                            self.gagnant = self.joueurs[self.jouant]
                            return

        if not case_vide_restante:
            self.gagnant = "egalite"
    
    def Start(self):
        self.Afficher()
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