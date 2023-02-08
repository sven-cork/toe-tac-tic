

game_board = ["-","-","-",
              "-","-","-"
              "-","-","-"]

print(game_board)


def select_player():
    player = ""
    while player != "X" or player != "O": 
        player = input("Player select team 'X' or 'O'")


def user_input(game_board):
    """
    User selects slot to place X or O. Checks if slot already taken and if so 
    prompts user to select a new slow.
    """

    user_input = int(input("Select a free slot (number 1-9) on the game board to achive three in a row: "))
    if user_input >= 1 and user_input <= 9 and game_board[user_input] != "-":
        game_board[user_input] = 