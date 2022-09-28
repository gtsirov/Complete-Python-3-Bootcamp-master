# Initialise global variables:
board_map = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}


def game_on():
    # Initialise variables
    result = "INVALID"

    # Ask for user input
    while result not in ["Y", "N"]:
        result = input("Would you like to play the Tic Tac Toe game? [Y or N]")

        if result not in ["Y", "N"]:
            print("Input out of range, please try again...")

    return result == "Y"


def choose_symbol():
    # Initialise variables
    result = "INVALID"

    # Ask for user input
    while result not in ["X", "O"]:
        result = input("Select your symbol? [X or O]")

        if result not in ["X", "O"]:
            print("Input out of range, please try again...")

    return result


def choose_board_position():
    global board_map
    # Initialise variables
    result = "INVALID"
    board_positions = []
    position_empty = False
    for i in range(1, 10):
        board_positions.append(str(i))
    # Check if input is a number between 1 and 9
    while not (result in board_positions and position_empty):
        result = input("Select a position on the board by using the keypad [1 to 9]")
        if result not in board_positions:
            print("Input out of range, please try again...")
        # Check if input position on the board is empty
        elif board_map[result] != " ":
            print("This board position is already taken, please try again...")
        else:
            position_empty = True
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
    global board_map
    board_map[str(pos)] = sym
    # Check for a winner
    if board_map["1"] == board_map["2"] == board_map["3"] == sym or \
            board_map["4"] == board_map["5"] == board_map["6"] == sym or \
            board_map["7"] == board_map["8"] == board_map["9"] == sym or \
            board_map["1"] == board_map["4"] == board_map["7"] == sym or \
            board_map["2"] == board_map["5"] == board_map["8"] == sym or \
            board_map["3"] == board_map["6"] == board_map["9"] == sym or \
            board_map["1"] == board_map["5"] == board_map["9"] == sym or \
            board_map["3"] == board_map["5"] == board_map["7"] == sym:
        #print("Winner!!!")
        return "winner"
    for k in board_map.keys():
        if board_map[k] == " ":
            return "continue"
    else:
        return "end"


while game_on():
    result = "play"
    clear_board()
    print("Player 1 will go first.")
    p1_symbol = choose_symbol()
    if p1_symbol == "O":
        p2_symbol = "X"
    else:
        p2_symbol = "O"
    print(f"Player 1 symbol is {p1_symbol} and Player 2 symbol is {p2_symbol}.")
    display_board(board_map)
    while result != "end":
        print(f"Player 1 it is your turn...")
        p1_position = choose_board_position()
        result = update_board(p1_position, p1_symbol)
        display_board(board_map)
        if result == "winner":
            print(f"Player 1 won the game!")
            break
        print(f"Player 2 it is your turn...")
        p2_position = choose_board_position()
        result = update_board(p2_position, p2_symbol)
        display_board(board_map)
        if result == "winner":
            print(f"Player 2 won the game!")
            break
