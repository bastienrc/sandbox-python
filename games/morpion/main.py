import tkinter

def check_nul():
    print("Match Nul")


def print_winner():
    global win

    if win is False:
        win = True

    print(f"Le joueur {current_player} a gagné le jeu !!!")


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player= "X"


def check_win(clicked_row, clicked_column):
    # Detection de la victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        # print("Victoire Horizontalement")
        print_winner()

    # Detection de la victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_column][i]
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        # print("Victoire Verticalement")
        print_winner()

    # Detection de la victoire diagonal
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        # print("Victoire diagonalement")
        print_winner()

    # Detection de la victoire diagonal inverse
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        # print("Victoire diagonalement inversé")
        print_winner()

    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button["text"] == "X" or current_button["text"] == "O":
                    count += 1
        print(count)
        if count == 9:
            check_nul()


def place_symbol(row, column):
    print("click", row, column)

    clicked_button = buttons[column][row]
    if clicked_button["text"] == "":
        clicked_button.config(text=current_player)

        check_win(row, column)
        switch_player()


def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root,
                font=("Arial", 42),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)


# Stockages
buttons = []
current_player = "X"
win = False

# Création de la fenêtre du jeu
root = tkinter.Tk()

# Personalisation de la fenêtre
root.title("Morpion")
root.minsize(500, 500)

draw_grid()

root.mainloop()
