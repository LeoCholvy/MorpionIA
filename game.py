from numpy import place


def Humain():
    a = int(input("Entrez x : "))
    b = int(input("Entrez y : "))
    return (a,b)

def Action(grille, coord, player, win):
    x,y = coord
    if grille[x][y] == 0:
        grille[x][y] = player

        for i in range(5):
            for j in range(5):
                if grille[i][j] == 0:
                    if not(x-2 <= i and i <= x+2) or not(y-2 <= j and j <= y+2):
                        grille[i][j] = 4
                    

    return grille, win

def Afficher(grille):
    for i in grille:
        print (i)
        print ()

def Main():
    grille = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

    player = 2
    win = True
    Afficher(grille)
    while win:
        if player == 1:
            player = 2
        else:
            player = 1
        print("Joueur "+str(player))
        grille, win = Action(grille, Humain(),player,win)
        Afficher(grille)

    print("Le joueur "+str(player)+" a gagné")

Main()