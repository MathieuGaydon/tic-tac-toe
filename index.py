#Creating and setting game variables to zero
current_player =""
grid=["-","-","-",
        "-","-","-",
        "-","-","-"]
end_game=  False
winner=''

#Creation of the game function to run the game program

def game():
    select_player()
    display_grid( )
    while end_game ==False :
        round (current_player)
        check_end_game()
        next_player()
    result()

#Creation of the player select function deciding who is player X and who is player O

def select_player():
    global current_player
    current_player =input ("please choose a cross (X) or a circle (O) :")
    while True:
        current_player = current_player.upper()
        if current_player =="X" :
            print("you have chosen X.player 2 will have O")
            break
        elif current_player =="O" :
            print("you have chosen O.player 2 will have X")
            break
        else :
            current_player=input("please choose a cross (X) or a circle (O) :")

# Création de la fonction affichage grille permettant l'affichage de notre grille ainsi que ses coordonnées

def display_grid() :
    print("\n")
    print("-----------------")
    print("|",grid[0],"|","|",grid[1],"|","|",grid[2],"|           |1|2|3|")
    print("-----------------")
    print("|",grid[3],"|","|",grid[4],"|","|",grid[5],"|           |4|5|6|")
    print("-----------------")
    print("|",grid[6],"|","|",grid[7],"|","|",grid[8],"|           |7|8|9|")
    print("-----------------")
    print("\n")

# Creation of the round function for changing players 
# And check that it enters a coordinate defined between 0 and 9

def round(player) :
    print("It's the player's round:" ,player)
    pos =input("please select an empty space on the grid between 0 and 9 : ")

    valide =False
    while valide == False :
        
        while pos not in ["1","2","3","4","5","6","7","8","9"] :
            pos =input("please select an empty space on the grid between 0 and 9 :")
        pos = int(pos) -1
        

        if grid[pos] =="-" :
             valide=True
        else :
            print("you cannot access this position")
    
    grid[pos] = player
    display_grid()

# Creation of an end-of-game check function to find out the outcome of the game

def check_end_game():
    check_victory()
    check_draw()

#Création de la fonction vérifier victoire permettant de vérifier 
# whether a player has won the game in rows, columns or diagonals

def check_victory() :
    global end_game
    global winner

    if grid[0] == grid[1] == grid [2] and grid [1] !="-":
        end_game=True
        winner=grid[1]
    if grid[3] == grid[4] == grid [5] and grid [3] !="-":
        end_game=True
        winner=grid[4]
    if grid[6] == grid[7] == grid [8] and grid [7] !="-":
        end_game=True
        winner=grid[7]
    if grid[0] == grid[3] == grid [6] and grid [3] !="-":
        end_game=True
        winner=grid[6]
    if grid[1] == grid[4] == grid [7] and grid [4] !="-":
        end_game=True
        winner=grid[7]
    if grid[2] == grid[5] == grid [8] and grid [5] !="-":
        end_game=True
        winner=grid[5]
    if grid[0] == grid[4] == grid [8] and grid [4] !="-":
        end_game=True
        winner=grid[4]
    if grid[2] == grid[4] == grid [6] and grid [2] !="-":
        end_game=True
        winner=grid[2]

#Creation of the check draw variable, which checks whether either player
#won and sent "that's a draw"

def check_draw() :
    global end_game
    if "-" not in grid :
        end_game = True
def next_player() :
    global current_player
    if current_player == "X" :
        current_player ="O"
    else :
        current_player ="X"
def result() :
    if winner =="X" or winner == "O" :
        print("The player :",winner,"has won")
    else :
        print("That's a draw")

#reminder of the game function used to launch the game
game()