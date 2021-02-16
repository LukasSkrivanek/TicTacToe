
game_still_going = True
winner = None
current_player = 'X'
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"
         ]


def display_rulles():
    separator = '=' * 35
    print(
        f"{separator}",
        f"Welcome to Tic Taco Toe",
        f"GAME RULES:",
        f"Each player can place one mark (or stone) per turn on the 3x3 grid",
        f"The WINNER is who succeeds in placing three of their marks in a",
        f"* Horizontal,",
        f"* verical or",
        f"* diagnosal row",
        f"Let's start the game",
        f"{separator}",
        sep='\n'
    )


def display_board():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")


def handle_turn(player):
    print(player + "'s turn.")
    valid = False
    while not valid:
        while True:
            try:
                position = int(input(" Choose a position from 1-9: ")) - 1
                if board[position] == "-":
                    valid = True
                else:
                    print("You can't go there. Go again.")
                if position in range(0, 9):
                    break
                else:
                    position = int(input("Invalid input. Choose a position from 1-9: ")) - 1
            except ValueError:
                print("Please write only numbers")
                continue

    board[position] = player
    display_board()


def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_draw():
    global game_still_going
    if '-' not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def main():
    display_rulles()
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_win()
        check_draw()
        flip_player()
        if winner == 'X' or winner == 'O':
            print(winner + " " + "won.")
        elif '-' not in board and winner == None:
            print("It's draw.")


if __name__ == "__main__":
    main()
