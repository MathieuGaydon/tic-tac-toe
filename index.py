#Création des variables du jeu et les mettre à zéro
joueur_actuel =""
grille=["-","-","-",
        "-","-","-",
        "-","-","-"]
fin_jeu=  False
gagnant=''

#création de la fonction jouer permettant l'éxécution du programme du jeu

def jouer():
    choix_joueur()
    affichage_grille( )
    while fin_jeu ==False :
        tour (joueur_actuel)
        verifier_fin_jeu()
        joueur_suivant()
    resultat()

#Création de la fonction choix joueur décidant qui est le joueur X et qui est le joueur O

def choix_joueur():
    global joueur_actuel
    joueur_actuel =input ("veuillez choissir une croix(X) ou un rond (O) :")
    while True:
        joueur_actuel = joueur_actuel.upper()
        if joueur_actuel =="X" :
            print("vous avez choisi X.le joueur 2 aura O")
            break
        elif joueur_actuel =="O" :
            print("vous avez choisi X.le joueur 2 aura O")
            break
        else :
            joueur_actuel=input("veuillez choissir une croix(X) ou un rond (O) :")

# Création de la fonction affichage grille permettant l'affichage de notre grille ainsi que ses coordonnées

def affichage_grille() :
    print("\n")
    print("-----------------")
    print("|",grille[0],"|","|",grille[1],"|","|",grille[2],"|           |1|2|3|")
    print("-----------------")
    print("|",grille[3],"|","|",grille[4],"|","|",grille[5],"|           |4|5|6|")
    print("-----------------")
    print("|",grille[6],"|","|",grille[7],"|","|",grille[8],"|           |7|8|9|")
    print("-----------------")
    print("\n")

# création de la fonction tour permettant de changer de joueur 
# et vérifier qu'il rentre une coordonnée défini entre 0 et 9

def tour(joueur) :
    print("C'est le tour du joueur :" ,joueur)
    pos =input("veuillez sélectionner un espace vide sur la grille entre 0 et 9 : ")

    valide =False
    while valide == False :
        
        while pos not in ["1","2","3","4","5","6","7","8","9"] :
            pos =input("veuillez sélectionner un espace vide sur la grille entre 0 et 8 :")
        pos = int(pos) -1
        

        if grille[pos] =="-" :
             valide=True
        else :
            print("vous ne pouvez pas accéder à cette position  ")
    
    grille[pos] = joueur
    affichage_grille()

# Création de la fonction vérifier fin de jeu pour savoir qu'elle est l'issu de la partie

def verifier_fin_jeu():
    verifier_victoire()
    verifier_match_nul()

#Création de la fonction vérifier victoire permettant de vérifier 
# si un joueur à gagner la partie en ligne ou en colonnes ou en diagonales

def verifier_victoire() :
    global fin_jeu
    global gagnant

    if grille[0] == grille[1] == grille [2] and grille [1] !="-":
        fin_jeu=True
        gagnant=grille[1]
    if grille[3] == grille[4] == grille [5] and grille [3] !="-":
        fin_jeu=True
        gagnant=grille[4]
    if grille[6] == grille[7] == grille [8] and grille [7] !="-":
        fin_jeu=True
        gagnant=grille[7]
    if grille[0] == grille[3] == grille [6] and grille [3] !="-":
        fin_jeu=True
        gagnant=grille[6]
    if grille[1] == grille[4] == grille [7] and grille [4] !="-":
        fin_jeu=True
        gagnant=grille[7]
    if grille[2] == grille[5] == grille [8] and grille [5] !="-":
        fin_jeu=True
        gagnant=grille[5]
    if grille[0] == grille[4] == grille [8] and grille [4] !="-":
        fin_jeu=True
        gagnant=grille[4]
    if grille[2] == grille[4] == grille [6] and grille [2] !="-":
        fin_jeu=True
        gagnant=grille[2]

#Création de la variables vérifier match nul qui vérifie si aucun des deux joueur
#n'a gagner et envoie "match nul"

def verifier_match_nul() :
    global fin_jeu
    if "-" not in grille :
        fin_jeu = True
def joueur_suivant() :
    global joueur_actuel
    if joueur_actuel == "X" :
        joueur_actuel ="O"
    else :
        joueur_actuel ="X"
def resultat() :
    if gagnant =="X" or gagnant == "O" :
        print("le joueur :",gagnant,"a gagné")
    else :
        print("match nul")

# rappel de la fonction jouer qui permet de lancé la partie
jouer()