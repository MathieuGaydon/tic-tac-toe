import tkinter

def check_nul():
    print("Match nul")


def print_winner():
    global win
    if win is False:
        win = True
        print("Le joueur", current_player, "a gagné le jeux !")


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else: 
        current_player = 'X'


def check_win(click_row, clicked_col):
    # detecting horizontal victory
    count = 0
    for i in range(3):
        current_button = buttons[i][click_row]

        if current_button['text'] == current_player:
            count += 1
    if count == 3: 
        print_winner()

    # detecting verticaly victory
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3: 
        print_winner()

    
    # detecting victory diagonally
    count = 0
    for i in range(3):
        current_button = buttons[i][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3: 
        print_winner()


    # detecting victory on the reverse diagonal
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3: 
        print_winner()
 

    if win is False: 
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == 'O':
                    count += 1
        if count == 9:
            print("Match nul !")


def place_symbol(row, column):
    print("click", row, column)

    clicked_button = buttons[column][row]
    if clicked_button['text'] == "":
        clicked_button.config(text=current_player)

    check_win(row, column)
    switch_player()

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 20),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
                )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)


# storage
buttons = []
current_player = 'X'
win = False

#  create the game window
root = tkinter.Tk()

# window customization
root.title("TicTacToe")
root.minsize(50, 50)


draw_grid()
root.mainloop()