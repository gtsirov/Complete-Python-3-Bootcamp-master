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


choose_board_position()
