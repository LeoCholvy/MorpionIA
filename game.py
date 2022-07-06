# Demande un coordonnée ou jouer à un joueur humain dans le terminal
def Humain():
    a = int(input("Entrez x : "))
    b = int(input("Entrez y : "))
    return (a,b)

# Action du joueur
# prend le joueur et la coordonée jouée puis retourne la nouvelle grille et la victoire
def Action(grille, coord, player, win):
    x,y = coord #coordonnée jouée
    if grille[x][y] == 0: #si la case est vide
        grille[x][y] = player #on indique que la case est occupée par le joueur

        #on vérifie si le joueur a gagné +
        if grille[x-2][y] == player and grille[x-1][y] == player:
            win = False
        if grille[x-1][y] == player and grille[x+1][y] == player:
            win = False
        if grille[x+1][y] == player and grille[x+2][y] == player:
            win = False
        if grille[x][y-2] == player and grille[x][y-1] == player:
            win = False
        if grille[x][y-1] == player and grille[x][y+1] == player:
            win = False
        if grille[x][y+1] == player and grille[x][y+2] == player:
            win = False
        
        #on vérifie si le joueur a gagné x
        if grille[x-2][y-2] == player and grille[x-1][y-1] == player:
            win = False
        if grille[x-1][y-1] == player and grille[x+1][y+1] == player:
            win = False
        if grille[x+1][y+1] == player and grille[x+2][y+2] == player:
            win = False
        if grille[x+2][y-2] == player and grille[x+1][y-1] == player:
            win = False
        if grille[x+1][y-1] == player and grille[x-1][y+1] == player:
            win = False
        if grille[x-1][y+1] == player and grille[x-2][y+2] == player:
            win = False
        
        #on indique les cases ou l'on ne peut plus jouer
        for i in range(5):
            for j in range(5):
                if grille[i][j] == 0:
                    if not(x-2 <= i and i <= x+2) or not(y-2 <= j and j <= y+2):
                        grille[i][j] = 4

    return grille, win

# affiche la grille en cours dans le terminal
def Afficher(grille):
    for i in grille:
        print (i)
        print ()

# initialise la partie
# le jeu se joue sur une grille de 5x5
# le joueur 1 commence
# les cases occupées par les joueurs doit pouvoir rentrer dans une grille en 3x3
# un joueur gagne en alignant 3 cases a lui
def Main():
    #grille en 5x5
    grille = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

    #joueur 1 commence
    player = 2
    win = True
    Afficher(grille)
    duree = 0
    while win:
        duree += 1
        if player == 1:
            player = 2
        else:
            player = 1
        print("Joueur "+str(player))
        #on demande une coordonnée
        grille, win = Action(grille, Humain(),player,win)
        Afficher(grille)

    #affiche les scores
    print("Le joueur "+str(player)+" a gagné")
    print("Durée : "+str(duree)+" tours")

Main()