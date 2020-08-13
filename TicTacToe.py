board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

num_board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9", ]

game_still_going = True
current_player = 'X'
winner = None


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def print_num_board():
    print(num_board[0] + " | " + num_board[1] + " | " + num_board[2])
    print(num_board[3] + " | " + num_board[4] + " | " + num_board[5])
    print(num_board[6] + " | " + num_board[7] + " | " + num_board[8])


def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

    return current_player


def choose_number(player):
    print(player + "'s turn")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:
        if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Choose a position from 1 to 9: ")

        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print("You can't put there, select another position !")

    board[position] = player
    num_board[position] = " "

    print_board()
    print_num_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    r = rows()
    c = columns()
    d = diagonals()

    if d:
        winner = d
    elif r:
        winner = r
    elif c:
        winner = c

    else:
        winner = None


def rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

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


def columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    if column_1 or column_3 or column_2:
        game_still_going = False
    else:
        return None


def diagonals():

    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    if diagonal_1 or diagonal_2:
        game_still_going = False
    else:
        return None


def check_if_tie():

    global game_still_going
    if '-' not in board:
        game_still_going = False
        return True
    else:
        return False


def play_game():

    print_board()
    print_num_board()

    while game_still_going:

        choose_number(current_player)

        check_if_game_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner + " won")

    elif winner == None:
        print("Tie")


play_game()
