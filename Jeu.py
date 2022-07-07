#Permet de copier n'importe quel objet
import copy
#Importation d'un perceptron Multi-Couche
from sklearn.neural_network import MLPClassifier
import numpy as np
#Génère des nombres aléatoires
import random
#Importation des fonctions de prétraitement des données
from sklearn import preprocessing
#Importation d'une forêt d'arbre décisionnels
from sklearn.ensemble import RandomForestClassifier
#Importation des arbres de décisions
from sklearn import tree

class Cringe_Morpion:
    def __init__(self):
        self.grille = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        class Joueur:
            def __init__(self, nom, score, numero, type):
                self.nom = nom
                self.score = score
                self.numero = numero
                self.victoires = 0
                self.type = type
            def Ajouter_score(self, score):
                self.score += score
        self.joueurs = [Joueur("Alphonse", 0, 7, "ai"), Joueur("p'tit Gil", 0, 2, "humain")]
        self.jouant = random.randint(0, 1)

        self.egalites = 0
        self.duree = 0
        self.gagnant = "nope"

        #Création d'une base d'observations qui contiendra l'historique des parties jouées
        self.base_de_jeu=[]
        #Création d'une base de résultats contiendra l'historique des résultats des parties jouées
        self.base_resultat_jeu=[]
        #Création d'un classifieur de type Arbre de décision
        #self.clf = tree.DecisionTreeClassifier()
        #Création d'un classifieur de type réseau de neurones
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6, 2), random_state=1)
        #Création d'un classifieur de type RandomForest
        #self.clf = RandomForestClassifier(n_estimators=50, max_depth=2,random_state=0)

    def Reset(self):
        self.grille = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        for k in self.joueurs:
            k.score = 0
        self.jouant = random.randint(0, 1)
        self.duree = 0
        self.gagnant = "nope"

    def train_ai_player(self):
        # Normalisation des données (absolument nécessaire pour un réseau de neurones)
        self.scaler = preprocessing.StandardScaler().fit(self.base_de_jeu)
        X_train=self.scaler.transform(self.base_de_jeu) 
        #Entrainement du classifieur chargé de choisir les coups de l'IA
        self.clf.fit ( X_train,self.base_resultat_jeu)

    #Fonction d'entraînement par renforcement de l'ia, elle fera l'ia jouer de nombreuse fois contre un joueur aléatoire
    def train_ai_jeu(self):
        #L'IA va jouer 10 fois 10000 jeu pour apprendre
        for i in range (0, 10):
            # Pour j allant de zéro à 10000
            for j in range (0,10000):
                #IA joue une partie 
                sauvegarde_plateaux, result = self.Start()
                
                #Pour tout les plateau de la dernière partie jouée
                for k in range (0,len(sauvegarde_plateaux)):
                    #La plateau sous forme de matrice de 5 x 5 est passé en vecteur de taille 25
                    sauvegarde_plateaux[k]=np.array(sauvegarde_plateaux[k]).reshape(-1)
                    #l'ensemble des données alphabétiques son convertie en données numériques
                    sauvegarde_plateaux[k]=self.convert_plateau(sauvegarde_plateaux[k])
                    sauvegarde_plateaux[k]=sauvegarde_plateaux[k].astype(np.float64)
                    #Si J1 0 gagné
                    #FIXME IA Alphonse
                    if( result == "Alphonse"):
                        #Ajouts des plateau a la base d'observations
                        self.base_de_jeu.append(sauvegarde_plateaux[k])
                        #Ajout de 0 à la base de résultat pour dire que J1 à gagné sur ce plateau
                        self.base_resultat_jeu.append(0)
                    #Si l'IA a gagné 0
                    else:
                        #Ajouts des plateau a la base d'observations
                        self.base_de_jeu.append(sauvegarde_plateaux[k])
                        #Ajout de 1 à la base de résultat pour dire que J1 à gagné sur ce plateau
                        self.base_resultat_jeu.append(1)

            #Affichage des victoires après 10000 partie
            print ("Itération = ", i , " victoire J1 = ",victoire_j1, "victoire IA = ",victoire_ia, "egalite = ",egalite)
            #Actualisation de l'intelligence de l'ia
            self.train_ai_player()

    def Afficher(self):
        for i in self.grille:
            print (i)
            print ()

    def Victoire(self):
        if self.gagnant == "egalite":
            print("Egalité")
            for i in self.joueurs:
                i.score += -50
            self.egalites += 1
        else:
            gagnant = self.joueurs[self.gagnant]
            perdant = self.joueurs[self.gagnant -1]
            gagnant.Ajouter_score(100)
            gagnant.victoires += 1
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
        return False
    
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
    
    def Entrainement_mouv(self):
        mouv = [] #liste des mouvements possibles
        for i in range(5):
            for j in range(5):
                if self.grille[i][j] == 0:
                    mouv . append ((i,j))
        return mouv[random.randint(0,len(mouv)-1)]

    #Renvoie l'ensemble des mouvements possibles pour le joueur passé en paramètre
    def generateur_de_mouvement(self):
        #Déclaration d'une liste qui contiendra tout les mvts possible
        liste_mouvement_possible=[]
        #Pour tout les cases du plateau 
        for i in range (0, 5):
            for j in range (0, 5):
                #Si la case courante est vide
                if (self.grille[i][j]==0):
                    #Création d'un mouvement virtuel et ajout de celui-ci a la liste des mouvements possibles
                    virtual_plateau=copy.deepcopy(self.grille)
                    virtual_plateau[i][j]=self.joueurs[self.jouant].numero
                    liste_mouvement_possible.append([virtual_plateau,(i,j)])

        return liste_mouvement_possible
    
    #Permet à l'ia de jouer son tour
    def ai_player_joue(self,list_mvt_possible):
        #Copie des mouvement possibles 
        list_mvt_possible_copy=copy.deepcopy(list_mvt_possible)
        # Conversion de la copie des mouvement possibles en données numériques
        for i in range (0,len(list_mvt_possible_copy)):
            #FIXME : il faut que le plateau soit converti en données numériques
            list_mvt_possible_copy[i][0]=np.array(list_mvt_possible_copy[i][0]).astype(np.float64)
        #Normalisation des données des plateaux numériques
        X_test=self.scaler.transform(list_mvt_possible_copy[0]) 
        #L'IA calcul de la probabilité de gagner selon chacun des mouvement possible
        proba_success_mvt=self.clf.predict_proba(X_test)
        indice_mvt=0
        #Pour tout les probabilités de gagner des mouvements possible, on choisi la plus grande
        for i in range (0, len(proba_success_mvt)):
            if(proba_success_mvt[indice_mvt][1]<proba_success_mvt[i][1]):
                indice_mvt=i

        self.plateau=list_mvt_possible[indice_mvt][1]
    
    def Start(self):
        while self.gagnant == "nope":
            self.duree += 1

            if self.joueurs[self.jouant].type == "humain":
                x,y = self.Interface()
            elif self.joueurs[self.jouant].type == "entraineur":
                x,y = self.Entrainement_mouv()
            elif self.joueurs[self.jouant].type == "ai":
                x,y = self.ai_player_joue(self.generateur_de_mouvement())

            self.Action(x,y)
            
            if self.jouant == 0:
                self.jouant = 1
            else:
                self.jouant = 0
        self.Victoire()
 
        return self.grille, self.joueurs[self.gagnant].nom


morpion = Cringe_Morpion()
morpion.Start()