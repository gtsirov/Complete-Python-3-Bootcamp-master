from random import shuffle

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(my_list)
print(my_list)


def select_players_0():
    """
    Method to ask the user and select the number of virtual players for the game of War
    :return: int
    """
    while True:
        try:
            val = int(input("Select the number of virtual players for the game of War:"))
        except ValueError:
            print("Invalid user input (ValueError raised because you did not enter an integer), try again...")
        else:
            break


select_players_0()


def select_players():
    """
    Method to ask the user and select the number of virtual players for the game of War
    :return: int
    """
    val = "INVALID"
    while val not in ["2", "3", "4", "5", "6"]:
        val = input("Select the number of virtual players for the game of War (any number between 2 and 6):")
        if val not in ["2", "3", "4", "5", "6"]:
            print("Invalid user input, try again...")
    return int(val)

select_players()