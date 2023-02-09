

game_board = ["-","-","-",
              "-","-","-"
              "-","-","-"]

print(game_board)


#global variables:
#game_board
#player?

#functions:
#select_player
#select slot on board and update board
#winner
#computer turn
#winner


def select_player():

    """
    Let player select team "X" or "O". Checks if either of the valid teams (characters) have been selected and corrects for lower case entered character."
    """

    player = ""

    while True: 
        player = input("Player select team 'X' or 'O': ").upper()
        if player == "X" or player == "O":
            break
    print(player)
    return player
    


def user_input(game_board):
    """
    User selects slot to place X or O. Checks if slot already taken and if so 
    prompts user to select a new slow.
    """

    user_input = int(input("Select a free slot (number 1-9) on the game board to achive three in a row: "))
    if user_input >= 1 and user_input <= 9 and game_board[user_input] != "-":
        game_board[user_input] = player

select_player()