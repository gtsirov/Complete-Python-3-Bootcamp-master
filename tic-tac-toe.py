# Initialise global variables:
board_map = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}


def game_on():
    # Initialise variables
    result = "INVALID"

    # Ask for user input
    while result not in ["Y", "N"]:
        result = input("Would you like to play the Tic Tac Toe game? [Y or N]")

        if result not in ["Y", "N"]:
            print("Input invalid, please try again...")

    return result == "Y"


def choose_symbol():
    # Initialise variables
    result = "INVALID"

    # Ask for user input
    while result not in ["X", "O"]:
        result = input("Select your symbol? [X or O]")

        if result not in ["X", "O"]:
            print("Input invalid, please try again...")

    return result


def choose_board_position():
    # Initialise variables
    result = "INVALID"
    board_positions = []
    for i in range(1, 10):
        board_positions.append(str(i))
    # Ask for user input
    while result not in board_positions:
        result = input("Select a position on the board by using the keypad [1 to 9]")

        if result not in board_positions:
            print("Input invalid, please try again...")

    return int(result)


def display_board(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print(board["1"] + "|" + board["2"] + "|" + board["3"])


def clear_board():
    global board_map
    for k in board_map.keys():
        board_map[k] = " "


def update_board(pos, sym):
    pass


while game_on():
    clear_board()
    print("Player 1 will go first.")
    p1_symbol = choose_symbol()
    if p1_symbol == "O":
        p2_symbol = "X"
    else:
        p2_symbol = "O"
    print(f"Player 1 symbol is {p1_symbol} and Player 2 symbol is {p2_symbol}.")
    display_board(board_map)
    print(f"Player 1 it is your turn...")
    p1_position = choose_board_position()
    update_board(p1_position, p1_symbol)
