from numpy import place


def Humain():
    a = int(input("Entrez x : "))
    b = int(input("Entrez y : "))
    return (a,b)

def Action(grille, coord, player, win):
    x,y = coord
    if grille[x][y] == 0:
        grille[x][y] = player

        print(grille[x][y-2], grille[x][y-1])

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
    duree = 0
    while win:
        duree += 1
        if player == 1:
            player = 2
        else:
            player = 1
        print("Joueur "+str(player))
        grille, win = Action(grille, Humain(),player,win)
        Afficher(grille)

    print("Le joueur "+str(player)+" a gagné")
    print("Durée : "+str(duree)+" tours")

Main()